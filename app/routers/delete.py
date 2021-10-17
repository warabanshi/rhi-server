from fastapi import APIRouter, Depends
from typing import Any, Dict, List

from app.dependencies import headers
from app.libraries.storage import update, retrieve_all


router = APIRouter(
    prefix="/delete",
    tags=["delete"],
    responses={404: {"description": "Not found"}},
)


@router.delete("/{command_nums_csv}")
async def delete(command_nums_csv: str, headers: Dict = Depends(headers)):
    def not_num_range(x: int):
        return not 0 <= x < len(original_data)

    command_nums: List[int] = [int(num) - 1 for num in command_nums_csv.split(",")]
    original_data: List[Dict[str, Any]] = retrieve_all(headers["x_rhi_username"])

    if any([not_num_range(n) for n in command_nums]):
        return {"result": "desired command numbers includes invalid one"}

    target_data = [v for k, v in enumerate(original_data) if k not in command_nums]
    update(headers["x_rhi_username"], target_data)

    return {"result": f"command {command_nums_csv} were deleted"}
