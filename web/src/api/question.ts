import { UIContextType } from '@/lib/ui.context';
import withAxios from './request'
import { QuestionRequest, AnswerResponse } from '@/lib';


export async function submitQuestion(ui: UIContextType, question: QuestionRequest): Promise<AnswerResponse> {
    const resp = await withAxios(ui).post('/question', question);
    return AnswerResponse.with(resp);
  }
  