import pytest
from backend.graph import retrieve, generate, grade_documents, transform_query, web_search, route_question, decide_to_generate, grade_generation_v_documents_and_question

# Sample state for testing
sample_state = {
    "question": "What is the capital of France?",
    "documents": []
}

# Test cases for the graph functions
class TestGraphFunctions:
    
    def test_retrieve(self):
        """
        Test the retrieve function with a valid question.
        """
        # Given a sample state with a question
        state = {"question": "What is the capital of France?"}
        
        # When we call retrieve
        result = retrieve(state)
        
        # Then we should get documents related to the question
        assert "documents" in result
        assert isinstance(result["documents"], list)

    def test_generate(self):
        """
        Test the generate function with valid state.
        """
        # Given a sample state with documents
        state = {
            "question": "What is the capital of France?",
            "documents": ["Paris is the capital of France."]
        }
        
        # When we call generate
        result = generate(state)
        
        # Then we should get a generation in the result
        assert "generation" in result
        assert isinstance(result["generation"], str)

    def test_grade_documents_relevant(self):
        """
        Test the grade_documents function with relevant documents.
        """
        # Given a sample state with relevant documents
        state = {
            "question": "What is the capital of France?",
            "documents": [{"page_content": "Paris is the capital of France."}]
        }
        
        # When we call grade_documents
        result = grade_documents(state)
        
        # Then we should get filtered relevant documents
        assert len(result["documents"]) > 0

    def test_transform_query(self):
        """
        Test the transform_query function to rephrase a question.
        """
        # Given a sample state
        state = {
            "question": "What is the capital of France?",
            "documents": []
        }
        
        # When we call transform_query
        result = transform_query(state)
        
        # Then we should get a better question
        assert "question" in result
        assert result["question"] != state["question"]

    def test_route_question_web_search(self):
        """
        Test the route_question function to route to web search.
        """
        # Given a sample state
        state = {
            "question": "What is the capital of France?",
            "documents": []
        }
        
        # When we call route_question
        result = route_question(state)
        
        # Then we should route to web_search
        assert result == "web_search"

    def test_decide_to_generate_no_relevant_docs(self):
        """
        Test the decide_to_generate function when there are no relevant documents.
        """
        # Given a sample state with no relevant documents
        state = {
            "question": "What is the capital of France?",
            "documents": []
        }
        
        # When we call decide_to_generate
        result = decide_to_generate(state)
        
        # Then we should decide to transform the query
        assert result == "transform_query"

    def test_grade_generation_v_documents_and_question(self):
        """
        Test the grade_generation_v_documents_and_question function.
        """
        # Given a sample state with generation and documents
        state = {
            "question": "What is the capital of France?",
            "documents": ["Paris is the capital of France."],
            "generation": "The capital of France is Paris."
        }
        
        # When we call grade_generation_v_documents_and_question
        result = grade_generation_v_documents_and_question(state)
        
        # Then we should get a decision based on the grading
        assert result in ["useful", "not useful", "not supported"]
