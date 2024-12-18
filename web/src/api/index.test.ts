// Importing necessary modules for testing
import * as api from './index';

/**
 * Test suite for the API module
 */
describe('API Module', () => {

  // Test case for checking if request module is exported correctly
  test('should export request module', () => {
    // Check if the request module is defined
    expect(api.request).toBeDefined();
  });

  // Test case for checking if question module is exported correctly
  test('should export question module', () => {
    // Check if the question module is defined
    expect(api.question).toBeDefined();
  });

  // Test case for checking if non-existent module is not exported
  test('should not export non-existent module', () => {
    // Check if the non-existent module is undefined
    expect(api.nonExistentModule).toBeUndefined();
  });

  // Test case for checking if all exports are functions (assuming they are)
  test('should export all modules as functions', () => {
    // Check if request and question are functions
    expect(typeof api.request).toBe('function');
    expect(typeof api.question).toBe('function');
  });

});
