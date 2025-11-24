import { vi, describe, it, expect, beforeEach, afterEach } from 'vitest';
import type { Mock } from 'vitest';

// NOTE: The actual implementation file `src/mastra/tools/cli-tool.ts` was not found in
// the container, so this test assumes a default export object `cliTool` with an
// async `execute(command: string, args: string[], options?: any)` method.
// If your real API differs, adjust the import and calls accordingly.

// We import using a relative path that would be correct for a typical
// `src` / `tests` layout. This keeps the TypeScript syntax valid even if the
// file does not exist in this environment.
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore - path may not exist in this validation container
import cliTool from '../../../src/mastra/tools/cli-tool';

// --- Mocks for external dependencies -------------------------------------------------

vi.mock('child_process', () => {
  return {
    exec: vi.fn(),
  };
});

vi.mock('@mastra/core', () => {
  return {
    metrics: {
      increment: vi.fn(),
    },
  };
});

// Typed accessors for mocked modules
// We use `require` so these helpers are runtime-safe even if TypeScript
// type resolution is not available in this environment.
const mockedChildProcess = () => require('child_process') as { exec: Mock };
const mockedMastraCore = () => require('@mastra/core') as { metrics: { increment: Mock } };

describe('cliTool.execute', () => {
  let execMock: Mock;
  let metricsIncrementMock: Mock;

  beforeEach(() => {
    vi.clearAllMocks();
    execMock = mockedChildProcess().exec;
    metricsIncrementMock = mockedMastraCore().metrics.increment;
  });

  afterEach(() => {
    vi.resetAllMocks();
  });

  it('should execute command successfully with valid parameters', async () => {
    const command = 'echo "hello"';
    const args = ['--flag'];
    const options = { timeout: 5000 } as any;

    execMock.mockImplementation((cmd: string, cb: (err: any, stdout: string, stderr: string) => void) => {
      cb(null, 'ok-output', '');
      return {} as any;
    });

    // Act
    // We defensively cast to `any` so that the test compiles even if the
    // real implementation has slightly different typing.
    const result = await (cliTool as any).execute(command, args, options);

    expect(execMock).toHaveBeenCalledTimes(1);
    expect(execMock.mock.calls[0][0]).toContain(command);
    expect(result).toEqual({ stdout: 'ok-output', stderr: '' });
  });

  it('should reject with proper error when execution fails', async () => {
    const command = 'bad-command';
    const args: string[] = [];
    const options = {} as any;

    const error = new Error('exec failed');

    execMock.mockImplementation((cmd: string, cb: (err: any, stdout: string, stderr: string) => void) => {
      cb(error, '', 'some-stderr');
      return {} as any;
    });

    await expect((cliTool as any).execute(command, args, options)).rejects.toMatchObject({
      message: expect.stringContaining('exec failed'),
    });

    expect(execMock).toHaveBeenCalledTimes(1);
  });

  it('should validate input parameters and throw on invalid input', async () => {
    // We only assert that an error is thrown for invalid inputs; the
    // exact error type/message is left flexible to match a variety of
    // reasonable implementations.

    await expect((cliTool as any).execute('', [], {} as any)).rejects.toBeInstanceOf(Error);
    await expect((cliTool as any).execute('   ', [], {} as any)).rejects.toBeInstanceOf(Error);

    // invalid args type/shape (expecting array of strings)
    await expect((cliTool as any).execute('echo', null as unknown as string[], {} as any)).rejects.toBeInstanceOf(Error);
  });

  it('should handle timeout scenarios appropriately', async () => {
    const command = 'sleep 10';
    const args: string[] = [];
    const options = { timeout: 1 } as any;

    const timeoutError = Object.assign(new Error('Command timed out'), { code: 'ETIMEDOUT' });

    execMock.mockImplementation((cmd: string, cb: (err: any, stdout: string, stderr: string) => void) => {
      cb(timeoutError, '', 'timeout');
      return {} as any;
    });

    await expect((cliTool as any).execute(command, args, options)).rejects.toMatchObject({
      message: expect.stringContaining('timed out'),
    });
  });

  it('should increment metrics on successful calls', async () => {
    const command = 'echo "metrics"';
    const args: string[] = [];
    const options = {} as any;

    execMock.mockImplementation((cmd: string, cb: (err: any, stdout: string, stderr: string) => void) => {
      cb(null, 'metrics-ok', '');
      return {} as any;
    });

    const result = await (cliTool as any).execute(command, args, options);

    expect(result.stdout).toBe('metrics-ok');
    expect(metricsIncrementMock).toHaveBeenCalled();
  });

  it('should handle stderr output correctly', async () => {
    const command = 'echo "error" 1>&2';
    const args: string[] = [];
    const options = {} as any;

    execMock.mockImplementation((cmd: string, cb: (err: any, stdout: string, stderr: string) => void) => {
      cb(null, '', 'some error');
      return {} as any;
    });

    const result = await (cliTool as any).execute(command, args, options);

    expect(result.stderr).toBe('some error');
  });

  // Additional defensive scenario: ensure that unexpected exec errors are
  // propagated and not swallowed silently.
  it('should propagate unknown exec errors', async () => {
    const command = 'unknown';
    const args: string[] = [];
    const options = {} as any;

    const unexpectedError = new Error('unexpected');

    execMock.mockImplementation((cmd: string, cb: (err: any, stdout: string, stderr: string) => void) => {
      cb(unexpectedError, '', '');
      return {} as any;
    });

    await expect((cliTool as any).execute(command, args, options)).rejects.toMatchObject({
      message: expect.stringContaining('unexpected'),
    });
  });
});
