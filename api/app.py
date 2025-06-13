"""FastAPI application providing memory and agent endpoints."""

from fastapi import FastAPI
from pydantic import BaseModel

from core.eidos_core import EidosCore
from agents.utility_agent import UtilityAgent
from agents.experiment_agent import ExperimentAgent


def create_app() -> FastAPI:
    """Return a configured FastAPI instance."""
    app = FastAPI(title="Eidos API")

    core = EidosCore()
    utility = UtilityAgent()
    experiment = ExperimentAgent()

    class MemoryItem(BaseModel):
        experience: str

    class TaskItem(BaseModel):
        task: str

    class HypothesisItem(BaseModel):
        hypothesis: str

    @app.post("/memory")
    async def add_memory(item: MemoryItem) -> dict[str, str]:
        """Store an experience in memory."""
        core.remember(item.experience)
        return {"status": "stored"}

    @app.get("/memory")
    async def get_memory() -> list:
        """Return all stored memories."""
        return core.reflect()

    @app.post("/agent/utility")
    async def run_utility(task: TaskItem) -> dict[str, str]:
        """Run a utility agent task."""
        result = utility.perform_task(task.task)
        return {"result": result}

    @app.post("/agent/experiment")
    async def run_experiment(data: HypothesisItem) -> dict[str, str]:
        """Run an experiment agent with a hypothesis."""
        result = experiment.run(data.hypothesis)
        return {"result": result}

    return app


app = create_app()
