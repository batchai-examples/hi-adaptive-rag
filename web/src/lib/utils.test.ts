"use client";

import { otEvent } from './utils';

describe('otEvent', () => {
  /**
   * Test case 1: Happy path - event has both preventDefault and stopPropagation methods
   * - Create a mock event object with both methods
   * - Call otEvent with the mock event
   * - Verify that both methods are called
   */
  test('should call preventDefault and stopPropagation when both methods exist', () => {
    const mockEvent = {
      preventDefault: jest.fn(),
      stopPropagation: jest.fn(),
    };
    
    otEvent(mockEvent);
    
    expect(mockEvent.preventDefault).toHaveBeenCalled();
    expect(mockEvent.stopPropagation).toHaveBeenCalled();
  });

  /**
   * Test case 2: Happy path - event has only preventDefault method
   * - Create a mock event object with only preventDefault
   * - Call otEvent with the mock event
   * - Verify that preventDefault is called and stopPropagation is not called
   */
  test('should call preventDefault when only preventDefault method exists', () => {
    const mockEvent = {
      preventDefault: jest.fn(),
      stopPropagation: undefined,
    };
    
    otEvent(mockEvent);
    
    expect(mockEvent.preventDefault).toHaveBeenCalled();
    expect(mockEvent.stopPropagation).toBeUndefined();
  });

  /**
   * Test case 3: Happy path - event has only stopPropagation method
   * - Create a mock event object with only stopPropagation
   * - Call otEvent with the mock event
   * - Verify that stopPropagation is called and preventDefault is not called
   */
  test('should call stopPropagation when only stopPropagation method exists', () => {
    const mockEvent = {
      preventDefault: undefined,
      stopPropagation: jest.fn(),
    };
    
    otEvent(mockEvent);
    
    expect(mockEvent.stopPropagation).toHaveBeenCalled();
    expect(mockEvent.preventDefault).toBeUndefined();
  });

  /**
   * Test case 4: Negative case - event has neither preventDefault nor stopPropagation methods
   * - Create a mock event object with neither method
   * - Call otEvent with the mock event
   * - Verify that no errors are thrown
   */
  test('should not throw an error when neither method exists', () => {
    const mockEvent = {};
    
    expect(() => otEvent(mockEvent)).not.toThrow();
  });

  /**
   * Test case 5: Corner case - event is null
   * - Call otEvent with null
   * - Verify that no errors are thrown
   */
  test('should not throw an error when event is null', () => {
    expect(() => otEvent(null)).not.toThrow();
  });

  /**
   * Test case 6: Corner case - event is undefined
   * - Call otEvent with undefined
   * - Verify that no errors are thrown
   */
  test('should not throw an error when event is undefined', () => {
    expect(() => otEvent(undefined)).not.toThrow();
  });
});
