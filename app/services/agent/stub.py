"""This is an automatically generated file. Do not modify it.

This file was generated using `langgraph-gen` version 0.0.3.
To regenerate this file, run `langgraph-gen` with the source `yaml` file as an argument.

Usage:

1. Add the generated file to your project.
2. Create a new agent using the stub.

Below is a sample implementation of the generated stub:

```python
from typing_extensions import TypedDict

from stub import CustomAgent

class SomeState(TypedDict):
    # define your attributes here
    foo: str

# Define stand-alone functions
def investigador(state: SomeState) -> dict:
    print("In node: investigador")
    return {
        # Add your state update logic here
    }


def tools(state: SomeState) -> dict:
    print("In node: tools")
    return {
        # Add your state update logic here
    }


def retriever(state: SomeState) -> dict:
    print("In node: retriever")
    return {
        # Add your state update logic here
    }


def route_after_model(state: SomeState) -> str:
    print("In condition: route_after_model")
    raise NotImplementedError("Implement me.")


agent = CustomAgent(
    state_schema=SomeState,
    impl=[
        ("investigador", investigador),
        ("tools", tools),
        ("retriever", retriever),
        ("route_after_model", route_after_model),
    ]
)

compiled_agent = agent.compile()

print(compiled_agent.invoke({"foo": "bar"}))
"""

from typing import Callable, Any, Optional, Type

from langgraph.constants import START, END
from langgraph.graph import StateGraph


def CustomAgent(
    *,
    state_schema: Optional[Type[Any]] = None,
    config_schema: Optional[Type[Any]] = None,
    input: Optional[Type[Any]] = None,
    output: Optional[Type[Any]] = None,
    impl: list[tuple[str, Callable]],
) -> StateGraph:
    """Create the state graph for CustomAgent."""
    # Declare the state graph
    builder = StateGraph(
        state_schema, config_schema=config_schema, input=input, output=output
    )

    nodes_by_name = {name: imp for name, imp in impl}

    all_names = set(nodes_by_name)

    expected_implementations = {
        "investigador",
        "tools",
        "cip_loader",
        "should_end",
        "data_loader",
    }

    missing_nodes = expected_implementations - all_names
    if missing_nodes:
        raise ValueError(f"Missing implementations for: {missing_nodes}")

    extra_nodes = all_names - expected_implementations

    if extra_nodes:
        raise ValueError(
            f"Extra implementations for: {extra_nodes}. Please regenerate the stub."
        )

    # Add nodes
    builder.add_node("investigador", nodes_by_name["investigador"])
    builder.add_node("tools", nodes_by_name["tools"])
    builder.add_node("cip_loader", nodes_by_name["cip_loader"])
    builder.add_node("data_loader", nodes_by_name["data_loader"])

    # Add edges
    builder.add_edge(START, "data_loader")
    builder.add_edge("data_loader", "cip_loader")
    builder.add_edge("tools", "investigador")
    builder.add_edge("cip_loader", "investigador")
    builder.add_conditional_edges(
        "investigador",
        nodes_by_name["should_end"],
        {
            "tools": "tools",
            "end": END,
        },
    )
    return builder
