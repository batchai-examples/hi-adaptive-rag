"use client";

import { AnswerResponse } from './dto';

/**
 * Test suite for AnswerResponse class
 */
describe('AnswerResponse', () => {

    /**
     * Test case for static method with() - happy path
     * This test checks if the method correctly assigns the prototype
     * and returns the object when a valid object is passed.
     */
    it('should return an AnswerResponse object with valid input', () => {
        const input = { question: 'What is your name?', answer: 'John Doe' };
        const response = AnswerResponse.with(input);
        expect(response).toBeDefined(); // Check if response is defined
        expect(response.question).toBe('What is your name?'); // Check if question is correct
        expect(response.answer).toBe('John Doe'); // Check if answer is correct
    });

    /**
     * Test case for static method with() - negative case
     * This test checks if the method returns undefined when no object is passed.
     */
    it('should return undefined when no input is provided', () => {
        const response = AnswerResponse.with(undefined);
        expect(response).toBeUndefined(); // Check if response is undefined
    });

    /**
     * Test case for static method with() - corner case
     * This test checks if the method handles an empty object correctly.
     */
    it('should return an AnswerResponse object with an empty object', () => {
        const input = {};
        const response = AnswerResponse.with(input);
        expect(response).toBeDefined(); // Check if response is defined
        expect(response.question).toBeUndefined(); // Check if question is undefined
        expect(response.answer).toBeUndefined(); // Check if answer is undefined
    });

    /**
     * Test case for static method with() - negative case
     * This test checks if the method handles null input correctly.
     */
    it('should return undefined when null is provided', () => {
        const response = AnswerResponse.with(null);
        expect(response).toBeUndefined(); // Check if response is undefined
    });

    /**
     * Test case for static method with() - happy path
     * This test checks if the method correctly assigns the prototype
     * and returns the object when a partially filled object is passed.
     */
    it('should return an AnswerResponse object with partial input', () => {
        const input = { question: 'What is your favorite color?' };
        const response = AnswerResponse.with(input);
        expect(response).toBeDefined(); // Check if response is defined
        expect(response.question).toBe('What is your favorite color?'); // Check if question is correct
        expect(response.answer).toBeUndefined(); // Check if answer is undefined
    });

    /**
     * Test case for static method with() - corner case
     * This test checks if the method handles an object with unexpected properties.
     */
    it('should return an AnswerResponse object with unexpected properties', () => {
        const input = { question: 'What is your age?', extra: 'not needed' };
        const response = AnswerResponse.with(input);
        expect(response).toBeDefined(); // Check if response is defined
        expect(response.question).toBe('What is your age?'); // Check if question is correct
        expect(response.answer).toBeUndefined(); // Check if answer is undefined
    });

});
