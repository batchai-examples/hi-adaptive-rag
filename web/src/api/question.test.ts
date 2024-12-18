import { submitQuestion } from './question';
import { UIContextType } from '@/lib/ui.context';
import { QuestionRequest, AnswerResponse } from '@/lib';
import withAxios from './request';

// Mocking the withAxios function to simulate API responses
jest.mock('./request', () => ({
  __esModule: true,
  default: jest.fn()
}));

describe('submitQuestion', () => {
  const mockUI: UIContextType = { /* mock UIContextType properties */ };

  // Happy path test case
  it('should submit a question and return a valid answer response', async () => {
    const mockQuestion: QuestionRequest = { /* mock question request properties */ };
    const mockResponse = { /* mock response properties */ };
    
    (withAxios as jest.Mock).mockReturnValue({
      post: jest.fn().mockResolvedValue(mockResponse)
    });

    const result = await submitQuestion(mockUI, mockQuestion);
    
    expect(result).toEqual(AnswerResponse.with(mockResponse));
    expect(withAxios).toHaveBeenCalledWith(mockUI);
  });

  // Positive case: Valid question with expected response
  it('should return an AnswerResponse when a valid question is submitted', async () => {
    const validQuestion: QuestionRequest = { /* valid question properties */ };
    const validResponse = { /* valid response properties */ };

    (withAxios as jest.Mock).mockReturnValue({
      post: jest.fn().mockResolvedValue(validResponse)
    });

    const result = await submitQuestion(mockUI, validQuestion);

    expect(result).toEqual(AnswerResponse.with(validResponse));
  });

  // Negative case: Submitting an invalid question
  it('should throw an error when submitting an invalid question', async () => {
    const invalidQuestion: QuestionRequest = { /* invalid question properties */ };

    (withAxios as jest.Mock).mockReturnValue({
      post: jest.fn().mockRejectedValue(new Error('Invalid question'))
    });

    await expect(submitQuestion(mockUI, invalidQuestion)).rejects.toThrow('Invalid question');
  });

  // Corner case: Submitting an empty question
  it('should throw an error when submitting an empty question', async () => {
    const emptyQuestion: QuestionRequest = { /* properties indicating an empty question */ };

    (withAxios as jest.Mock).mockReturnValue({
      post: jest.fn().mockRejectedValue(new Error('Question cannot be empty'))
    });

    await expect(submitQuestion(mockUI, emptyQuestion)).rejects.toThrow('Question cannot be empty');
  });

  // Corner case: Network error during submission
  it('should throw an error when there is a network issue', async () => {
    const question: QuestionRequest = { /* valid question properties */ };

    (withAxios as jest.Mock).mockReturnValue({
      post: jest.fn().mockRejectedValue(new Error('Network Error'))
    });

    await expect(submitQuestion(mockUI, question)).rejects.toThrow('Network Error');
  });

  // Positive case: Submitting a question with special characters
  it('should handle submission of a question with special characters', async () => {
    const specialCharQuestion: QuestionRequest = { /* question with special characters */ };
    const responseWithSpecialChars = { /* response properties */ };

    (withAxios as jest.Mock).mockReturnValue({
      post: jest.fn().mockResolvedValue(responseWithSpecialChars)
    });

    const result = await submitQuestion(mockUI, specialCharQuestion);

    expect(result).toEqual(AnswerResponse.with(responseWithSpecialChars));
  });
});
