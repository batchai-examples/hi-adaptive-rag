"use client";

export class QuestionRequest {
    question: string;
}

export class AnswerResponse {
    question: string;
    answer: string;

    static with(obj: any): AnswerResponse {
        if (!obj) return;
        Object.setPrototypeOf(obj, AnswerResponse.prototype);
        return obj;
    }

}
