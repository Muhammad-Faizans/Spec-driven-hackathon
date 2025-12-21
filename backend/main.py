#!/usr/bin/env python3
"""
Main entry point for the AI Assistant.
Handles both content ingestion and chat modes.
Can be run as CLI or imported for FastAPI usage.
"""

import sys
import argparse
from ingest_local_docs import ingest_local_docs
from chat_gemini import query_qdrant, format_response


def run_chat_interface():
    """Run the command-line chat interface."""
    print("Physical AI & Humanoid Robotics Curriculum Assistant")
    print("Type 'quit' or 'exit' to stop the chat.\n")

    while True:
        try:
            query = input("You: ").strip()

            if query.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break

            if not query:
                continue

            print("Searching for relevant information...")
            search_results = query_qdrant(query)
            response = format_response(query, search_results)

            print(f"Assistant: {response}\n")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def run_ingest_process():
    """Run the content ingestion process."""
    print("Starting content ingestion process...")
    return ingest_local_docs()


def run_chat_process():
    """Run the chat interface process."""
    print("Starting chat interface...")
    run_chat_interface()


def main():
    # Only parse arguments if there are command line arguments provided
    # This allows the file to be imported without triggering argument parsing
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="AI Assistant for Physical AI & Humanoid Robotics Curriculum")
        parser.add_argument("mode", choices=["ingest", "chat"], help="Operation mode: ingest or chat")

        args = parser.parse_args()

        if args.mode == "ingest":
            run_ingest_process()
        elif args.mode == "chat":
            run_chat_process()
    else:
        # If no arguments provided, just import and make functions available
        # This allows the file to be imported for FastAPI without errors
        print("Main module loaded. Functions available for FastAPI.")


if __name__ == "__main__":
    main()