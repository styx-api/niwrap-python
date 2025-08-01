# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_LABEL2VOXEL_METADATA = Metadata(
    id="488fd9f6f8cf1cc2dafb238be876366f78aac9b2.boutiques",
    name="fsl_label2voxel",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


FslLabel2voxelParameters = typing.TypedDict('FslLabel2voxelParameters', {
    "__STYXTYPE__": typing.Literal["fsl_label2voxel"],
    "label_value": float,
    "labeled_volume": InputPathType,
    "src_volume": InputPathType,
    "output_filename": str,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "fsl_label2voxel": fsl_label2voxel_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "fsl_label2voxel": fsl_label2voxel_outputs,
    }.get(t)


class FslLabel2voxelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_label2voxel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_voxel_data: OutputPathType
    """Output voxel data based on the specified label value"""


def fsl_label2voxel_params(
    label_value: float,
    labeled_volume: InputPathType,
    src_volume: InputPathType,
    output_filename: str,
) -> FslLabel2voxelParameters:
    """
    Build parameters.
    
    Args:
        label_value: Label value to convert.
        labeled_volume: Labeled volume file.
        src_volume: Source volume file.
        output_filename: Output filename for voxel data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_label2voxel",
        "label_value": label_value,
        "labeled_volume": labeled_volume,
        "src_volume": src_volume,
        "output_filename": output_filename,
    }
    return params


def fsl_label2voxel_cargs(
    params: FslLabel2voxelParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("fsl_label2voxel")
    cargs.append(str(params.get("label_value")))
    cargs.append(execution.input_file(params.get("labeled_volume")))
    cargs.append(execution.input_file(params.get("src_volume")))
    cargs.append(params.get("output_filename"))
    return cargs


def fsl_label2voxel_outputs(
    params: FslLabel2voxelParameters,
    execution: Execution,
) -> FslLabel2voxelOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslLabel2voxelOutputs(
        root=execution.output_file("."),
        output_voxel_data=execution.output_file(params.get("output_filename")),
    )
    return ret


def fsl_label2voxel_execute(
    params: FslLabel2voxelParameters,
    execution: Execution,
) -> FslLabel2voxelOutputs:
    """
    Converts labeled volumes to voxels based on specified labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslLabel2voxelOutputs`).
    """
    params = execution.params(params)
    cargs = fsl_label2voxel_cargs(params, execution)
    ret = fsl_label2voxel_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_label2voxel(
    label_value: float,
    labeled_volume: InputPathType,
    src_volume: InputPathType,
    output_filename: str,
    runner: Runner | None = None,
) -> FslLabel2voxelOutputs:
    """
    Converts labeled volumes to voxels based on specified labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        label_value: Label value to convert.
        labeled_volume: Labeled volume file.
        src_volume: Source volume file.
        output_filename: Output filename for voxel data.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslLabel2voxelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_LABEL2VOXEL_METADATA)
    params = fsl_label2voxel_params(
        label_value=label_value,
        labeled_volume=labeled_volume,
        src_volume=src_volume,
        output_filename=output_filename,
    )
    return fsl_label2voxel_execute(params, execution)


__all__ = [
    "FSL_LABEL2VOXEL_METADATA",
    "FslLabel2voxelOutputs",
    "FslLabel2voxelParameters",
    "fsl_label2voxel",
    "fsl_label2voxel_params",
]
