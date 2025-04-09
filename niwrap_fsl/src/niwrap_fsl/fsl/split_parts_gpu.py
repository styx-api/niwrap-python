# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SPLIT_PARTS_GPU_METADATA = Metadata(
    id="bda890fb23c36ebbcf15c9ff09e5ac7bff39d458.boutiques",
    name="split_parts_gpu",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


SplitPartsGpuParameters = typing.TypedDict('SplitPartsGpuParameters', {
    "__STYX_TYPE__": typing.Literal["split_parts_gpu"],
    "datafile": InputPathType,
    "maskfile": InputPathType,
    "bvals_file": InputPathType,
    "bvecs_file": InputPathType,
    "grad_file": typing.NotRequired[str | None],
    "use_grad_file": int,
    "total_num_parts": int,
    "output_directory": str,
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
        "split_parts_gpu": split_parts_gpu_cargs,
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
        "split_parts_gpu": split_parts_gpu_outputs,
    }.get(t)


class SplitPartsGpuOutputs(typing.NamedTuple):
    """
    Output object returned when calling `split_parts_gpu(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_parts: OutputPathType
    """Output parts files"""


def split_parts_gpu_params(
    datafile: InputPathType,
    maskfile: InputPathType,
    bvals_file: InputPathType,
    bvecs_file: InputPathType,
    use_grad_file: int,
    total_num_parts: int,
    output_directory: str,
    grad_file: str | None = None,
) -> SplitPartsGpuParameters:
    """
    Build parameters.
    
    Args:
        datafile: Input data file.
        maskfile: Input mask file.
        bvals_file: bvals file.
        bvecs_file: bvecs file.
        use_grad_file: Use gradient file (0 or 1).
        total_num_parts: Total number of parts.
        output_directory: Output directory.
        grad_file: Gradient file (can be null).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "split_parts_gpu",
        "datafile": datafile,
        "maskfile": maskfile,
        "bvals_file": bvals_file,
        "bvecs_file": bvecs_file,
        "use_grad_file": use_grad_file,
        "total_num_parts": total_num_parts,
        "output_directory": output_directory,
    }
    if grad_file is not None:
        params["grad_file"] = grad_file
    return params


def split_parts_gpu_cargs(
    params: SplitPartsGpuParameters,
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
    cargs.append("split_parts_gpu")
    cargs.append(execution.input_file(params.get("datafile")))
    cargs.append(execution.input_file(params.get("maskfile")))
    cargs.append(execution.input_file(params.get("bvals_file")))
    cargs.append(execution.input_file(params.get("bvecs_file")))
    if params.get("grad_file") is not None:
        cargs.append(params.get("grad_file"))
    cargs.append(str(params.get("use_grad_file")))
    cargs.append(str(params.get("total_num_parts")))
    cargs.append(params.get("output_directory"))
    return cargs


def split_parts_gpu_outputs(
    params: SplitPartsGpuParameters,
    execution: Execution,
) -> SplitPartsGpuOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SplitPartsGpuOutputs(
        root=execution.output_file("."),
        output_parts=execution.output_file(params.get("output_directory") + "/part_*"),
    )
    return ret


def split_parts_gpu_execute(
    params: SplitPartsGpuParameters,
    execution: Execution,
) -> SplitPartsGpuOutputs:
    """
    Splits parts of data for GPU processing.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SplitPartsGpuOutputs`).
    """
    params = execution.params(params)
    cargs = split_parts_gpu_cargs(params, execution)
    ret = split_parts_gpu_outputs(params, execution)
    execution.run(cargs)
    return ret


def split_parts_gpu(
    datafile: InputPathType,
    maskfile: InputPathType,
    bvals_file: InputPathType,
    bvecs_file: InputPathType,
    use_grad_file: int,
    total_num_parts: int,
    output_directory: str,
    grad_file: str | None = None,
    runner: Runner | None = None,
) -> SplitPartsGpuOutputs:
    """
    Splits parts of data for GPU processing.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        datafile: Input data file.
        maskfile: Input mask file.
        bvals_file: bvals file.
        bvecs_file: bvecs file.
        use_grad_file: Use gradient file (0 or 1).
        total_num_parts: Total number of parts.
        output_directory: Output directory.
        grad_file: Gradient file (can be null).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SplitPartsGpuOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPLIT_PARTS_GPU_METADATA)
    params = split_parts_gpu_params(
        datafile=datafile,
        maskfile=maskfile,
        bvals_file=bvals_file,
        bvecs_file=bvecs_file,
        grad_file=grad_file,
        use_grad_file=use_grad_file,
        total_num_parts=total_num_parts,
        output_directory=output_directory,
    )
    return split_parts_gpu_execute(params, execution)


__all__ = [
    "SPLIT_PARTS_GPU_METADATA",
    "SplitPartsGpuOutputs",
    "SplitPartsGpuParameters",
    "split_parts_gpu",
    "split_parts_gpu_params",
]
