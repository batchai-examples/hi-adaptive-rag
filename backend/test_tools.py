import pytest
from backend.tools import build_index, build_question_router, build_retrieval_grader, build_hallucination_grader, build_answer_grader, build_question_rewriter

class TestTools:

    def test_build_index(self):
        """Test the build_index function to ensure it returns a VectorStoreRetriever."""
        # Step 1: Call the build_index function
        retriever = build_index()
        # Step 2: Assert that the returned object is an instance of VectorStoreRetriever
        assert isinstance(retriever, VectorStoreRetriever)

    def test_build_question_router(self):
        """Test the build_question_router function to ensure it returns a valid routing mechanism."""
        # Step 1: Call the build_question_router function
        router = build_question_router()
        # Step 2: Assert that the router can be invoked with a question
        response = router.invoke({"question": "What is agent memory?"})
        # Step 3: Assert that the response contains a valid datasource
        assert response['datasource'] in ["vectorstore", "web_search"]

    def test_build_retrieval_grader(self):
        """Test the build_retrieval_grader function to ensure it returns a valid grader."""
        # Step 1: Call the build_retrieval_grader function
        grader = build_retrieval_grader()
        # Step 2: Assert that the grader can be invoked with a document and question
        response = grader.invoke({"document": "This is a test document.", "question": "Is this relevant?"})
        # Step 3: Assert that the response is either 'yes' or 'no'
        assert response['binary_score'] in ['yes', 'no']

    def test_build_hallucination_grader(self):
        """Test the build_hallucination_grader function to ensure it returns a valid hallucination grader."""
        # Step 1: Call the build_hallucination_grader function
        grader = build_hallucination_grader()
        # Step 2: Assert that the grader can be invoked with documents and generation
        response = grader.invoke({"documents": "Fact 1. Fact 2.", "generation": "This is a generated answer."})
        # Step 3: Assert that the response is either 'yes' or 'no'
        assert response['binary_score'] in ['yes', 'no']

    def test_build_answer_grader(self):
        """Test the build_answer_grader function to ensure it returns a valid answer grader."""
        # Step 1: Call the build_answer_grader function
        grader = build_answer_grader()
        # Step 2: Assert that the grader can be invoked with a question and generation
        response = grader.invoke({"question": "What is the capital of France?", "generation": "The capital of France is Paris."})
        # Step 3: Assert that the response is either 'yes' or 'no'
        assert response['binary_score'] in ['yes', 'no']

    def test_build_question_rewriter(self):
        """Test the build_question_rewriter function to ensure it returns a valid question rewriter."""
        # Step 1: Call the build_question_rewriter function
        rewriter = build_question_rewriter()
        # Step 2: Assert that the rewriter can be invoked with a question
        response = rewriter.invoke({"question": "What is the role of memory in an agent's functioning?"})
        # Step 3: Assert that the response is a string (the rewritten question)
        assert isinstance(response, str)
