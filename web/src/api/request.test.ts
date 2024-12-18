import { UIContextType } from '@/lib/ui.context';
import axios from 'axios';
import withAxios from './request'; // Adjust the import path as necessary

// Mocking the UIContextType for testing
const mockUIContext: UIContextType = {
  setError: jest.fn(),
};

describe('withAxios', () => {
  let axiosInstance: any;

  beforeEach(() => {
    axiosInstance = withAxios(mockUIContext);
  });

  /**
   * Test case for a successful request
   * It should return the response data when the request is successful.
   */
  it('should return response data on successful request', async () => {
    // Mocking axios.get to return a successful response
    jest.spyOn(axios, 'create').mockReturnValue({
      interceptors: {
        request: { use: jest.fn() },
        response: { use: jest.fn() },
      },
      get: jest.fn().mockResolvedValue({ data: { message: 'Success' } }),
    });

    const response = await axiosInstance.get('/test');
    expect(response).toEqual({ message: 'Success' });
  });

  /**
   * Test case for handling 401 Unauthorized error
   * It should resolve to null when a 401 error occurs.
   */
  it('should resolve to null on 401 Unauthorized error', async () => {
    // Mocking axios.get to return a 401 error
    jest.spyOn(axios, 'create').mockReturnValue({
      interceptors: {
        request: { use: jest.fn() },
        response: { use: jest.fn() },
      },
      get: jest.fn().mockRejectedValue({
        response: { status: 401 },
      }),
    });

    const response = await axiosInstance.get('/test');
    expect(response).toBeNull();
  });

  /**
   * Test case for handling other errors
   * It should call setError on the UI context with the error message.
   */
  it('should call setError on other errors', async () => {
    const errorMessage = 'An error occurred';
    // Mocking axios.get to return a different error
    jest.spyOn(axios, 'create').mockReturnValue({
      interceptors: {
        request: { use: jest.fn() },
        response: { use: jest.fn() },
      },
      get: jest.fn().mockRejectedValue({
        response: { data: { error: 'Error', message: errorMessage } },
      }),
    });

    await expect(axiosInstance.get('/test')).rejects.toThrow(errorMessage);
    expect(mockUIContext.setError).toHaveBeenCalledWith('Error An error occurred');
  });

  /**
   * Test case for handling errors without a response
   * It should reject with the original error.
   */
  it('should reject with the original error if no response', async () => {
    const originalError = new Error('Network Error');
    // Mocking axios.get to return a network error
    jest.spyOn(axios, 'create').mockReturnValue({
      interceptors: {
        request: { use: jest.fn() },
        response: { use: jest.fn() },
      },
      get: jest.fn().mockRejectedValue(originalError),
    });

    await expect(axiosInstance.get('/test')).rejects.toThrow(originalError);
  });

  /**
   * Test case for checking request headers
   * It should set the Content-Type header to application/json.
   */
  it('should set Content-Type header to application/json', async () => {
    const axiosMock = jest.spyOn(axios, 'create').mockReturnValue({
      interceptors: {
        request: {
          use: (onFulfilled: Function) => {
            const config = { headers: {} };
            onFulfilled(config);
            expect(config.headers['Content-Type']).toBe('application/json');
          },
        },
        response: { use: jest.fn() },
      },
      get: jest.fn(),
    });

    axiosInstance.get('/test');
    expect(axiosMock).toHaveBeenCalled();
  });
});
