import pytest
from langgraph.graph import END, StateGraph, START
from graph import GraphState, web_search, retrieve, grade_documents, generate, transform_query, route_question, decide_to_generate, grade_generation_v_documents_and_question

# Initialize the workflow for testing
workflow = StateGraph(GraphState)

# Define the nodes for the workflow
workflow.add_node("web_search", web_search)
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("transform_query", transform_query)

# Build graph for testing
workflow.add_conditional_edges(
    START,
    route_question,
    {
        "web_search": "web_search",
        "vectorstore": "retrieve",
    },
)
workflow.add_edge("web_search", "generate")
workflow.add_edge("retrieve", "grade_documents")
workflow.add_conditional_edges(
    "grade_documents",
    decide_to_generate,
    {
        "transform_query": "transform_query",
        "generate": "generate",
    },
)
workflow.add_edge("transform_query", "retrieve")
workflow.add_conditional_edges(
    "generate",
    grade_generation_v_documents_and_question,
    {
        "not supported": "generate",
        "useful": END,
        "not useful": "transform_query",
    },
)

@pytest.fixture
def setup_workflow():
    """Fixture to set up the workflow for testing."""
    return workflow

def test_workflow_initialization(setup_workflow):
    """Test the initialization of the workflow."""
    # Check if the workflow has been initialized correctly
    assert setup_workflow is not None
    assert len(setup_workflow.nodes) == 5  # We have 5 nodes added

def test_workflow_edges(setup_workflow):
    """Test the edges of the workflow."""
    # Check if the edges are correctly established
    assert setup_workflow.has_edge(START, "web_search")
    assert setup_workflow.has_edge(START, "vectorstore")
    assert setup_workflow.has_edge("web_search", "generate")
    assert setup_workflow.has_edge("retrieve", "grade_documents")
    assert setup_workflow.has_edge("grade_documents", "transform_query")
    assert setup_workflow.has_edge("grade_documents", "generate")
    assert setup_workflow.has_edge("transform_query", "retrieve")
    assert setup_workflow.has_edge("generate", "not supported")
    assert setup_workflow.has_edge("generate", "useful")
    assert setup_workflow.has_edge("generate", "not useful")

def test_route_question_edge(setup_workflow):
    """Test the routing question edge."""
    # Ensure that the route_question function is correctly routed
    assert setup_workflow.has_edge(START, "web_search")
    assert setup_workflow.has_edge(START, "vectorstore")

def test_decide_to_generate_edge(setup_workflow):
    """Test the decision-making edge for generation."""
    # Check if the decision to generate leads to the correct nodes
    assert setup_workflow.has_edge("grade_documents", "transform_query")
    assert setup_workflow.has_edge("grade_documents", "generate")

def test_generate_edge_conditions(setup_workflow):
    """Test the conditions for the generate edge."""
    # Check if the generate edge leads to the correct outcomes
    assert setup_workflow.has_edge("generate", "not supported")
    assert setup_workflow.has_edge("generate", "useful")
    assert setup_workflow.has_edge("generate", "not useful")

def test_workflow_end_state(setup_workflow):
    """Test the end state of the workflow."""
    # Ensure that the workflow can reach the END state
    assert setup_workflow.has_edge("generate", END)
