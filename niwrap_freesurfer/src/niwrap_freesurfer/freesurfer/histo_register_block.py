# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

HISTO_REGISTER_BLOCK_METADATA = Metadata(
    id="a9ce2e4f5a3f5c4fa13464f62cf2766ed76dbba2.boutiques",
    name="histo_register_block",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


HistoRegisterBlockParameters = typing.TypedDict('HistoRegisterBlockParameters', {
    "__STYX_TYPE__": typing.Literal["histo_register_block"],
    "seg_time1": InputPathType,
    "seg_time2": InputPathType,
    "transform1": InputPathType,
    "transform2": InputPathType,
    "output_file": str,
    "out_like": typing.NotRequired[InputPathType | None],
    "invert_transform": bool,
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
        "histo_register_block": histo_register_block_cargs,
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
        "histo_register_block": histo_register_block_outputs,
    }.get(t)


class HistoRegisterBlockOutputs(typing.NamedTuple):
    """
    Output object returned when calling `histo_register_block(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    aligned_output: OutputPathType
    """Aligned output file"""


def histo_register_block_params(
    seg_time1: InputPathType,
    seg_time2: InputPathType,
    transform1: InputPathType,
    transform2: InputPathType,
    output_file: str,
    out_like: InputPathType | None = None,
    invert_transform: bool = False,
) -> HistoRegisterBlockParameters:
    """
    Build parameters.
    
    Args:
        seg_time1: Segmented image at time point 1.
        seg_time2: Segmented image at time point 2.
        transform1: Transformation file for time point 1.
        transform2: Transformation file for time point 2.
        output_file: Output file name for the aligned image.
        out_like: Set output volume parameters like the reference volume.
        invert_transform: Invert transform coordinates.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "histo_register_block",
        "seg_time1": seg_time1,
        "seg_time2": seg_time2,
        "transform1": transform1,
        "transform2": transform2,
        "output_file": output_file,
        "invert_transform": invert_transform,
    }
    if out_like is not None:
        params["out_like"] = out_like
    return params


def histo_register_block_cargs(
    params: HistoRegisterBlockParameters,
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
    cargs.append("histo_register_block")
    cargs.append(execution.input_file(params.get("seg_time1")))
    cargs.append(execution.input_file(params.get("seg_time2")))
    cargs.append(execution.input_file(params.get("transform1")))
    cargs.append(execution.input_file(params.get("transform2")))
    cargs.append(params.get("output_file"))
    if params.get("out_like") is not None:
        cargs.extend([
            "-out_like",
            execution.input_file(params.get("out_like"))
        ])
    if params.get("invert_transform"):
        cargs.append("-I")
    return cargs


def histo_register_block_outputs(
    params: HistoRegisterBlockParameters,
    execution: Execution,
) -> HistoRegisterBlockOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = HistoRegisterBlockOutputs(
        root=execution.output_file("."),
        aligned_output=execution.output_file(params.get("output_file")),
    )
    return ret


def histo_register_block_execute(
    params: HistoRegisterBlockParameters,
    execution: Execution,
) -> HistoRegisterBlockOutputs:
    """
    A tool to align a histological slice with a block face image.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `HistoRegisterBlockOutputs`).
    """
    params = execution.params(params)
    cargs = histo_register_block_cargs(params, execution)
    ret = histo_register_block_outputs(params, execution)
    execution.run(cargs)
    return ret


def histo_register_block(
    seg_time1: InputPathType,
    seg_time2: InputPathType,
    transform1: InputPathType,
    transform2: InputPathType,
    output_file: str,
    out_like: InputPathType | None = None,
    invert_transform: bool = False,
    runner: Runner | None = None,
) -> HistoRegisterBlockOutputs:
    """
    A tool to align a histological slice with a block face image.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        seg_time1: Segmented image at time point 1.
        seg_time2: Segmented image at time point 2.
        transform1: Transformation file for time point 1.
        transform2: Transformation file for time point 2.
        output_file: Output file name for the aligned image.
        out_like: Set output volume parameters like the reference volume.
        invert_transform: Invert transform coordinates.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `HistoRegisterBlockOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(HISTO_REGISTER_BLOCK_METADATA)
    params = histo_register_block_params(
        seg_time1=seg_time1,
        seg_time2=seg_time2,
        transform1=transform1,
        transform2=transform2,
        output_file=output_file,
        out_like=out_like,
        invert_transform=invert_transform,
    )
    return histo_register_block_execute(params, execution)


__all__ = [
    "HISTO_REGISTER_BLOCK_METADATA",
    "HistoRegisterBlockOutputs",
    "HistoRegisterBlockParameters",
    "histo_register_block",
    "histo_register_block_params",
]
