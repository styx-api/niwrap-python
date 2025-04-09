# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_TRANSPOSE_METADATA = Metadata(
    id="019d0e455ca5ac8bedcc9c8ae119758389ce31b1.boutiques",
    name="cifti-transpose",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


CiftiTransposeParameters = typing.TypedDict('CiftiTransposeParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-transpose"],
    "cifti_in": InputPathType,
    "cifti_out": str,
    "opt_mem_limit_limit_gb": typing.NotRequired[float | None],
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
        "cifti-transpose": cifti_transpose_cargs,
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
        "cifti-transpose": cifti_transpose_outputs,
    }.get(t)


class CiftiTransposeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_transpose(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_transpose_params(
    cifti_in: InputPathType,
    cifti_out: str,
    opt_mem_limit_limit_gb: float | None = None,
) -> CiftiTransposeParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: the input cifti file.
        cifti_out: the output cifti file.
        opt_mem_limit_limit_gb: restrict memory usage: memory limit in\
            gigabytes.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-transpose",
        "cifti_in": cifti_in,
        "cifti_out": cifti_out,
    }
    if opt_mem_limit_limit_gb is not None:
        params["opt_mem_limit_limit_gb"] = opt_mem_limit_limit_gb
    return params


def cifti_transpose_cargs(
    params: CiftiTransposeParameters,
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
    cargs.append("wb_command")
    cargs.append("-cifti-transpose")
    cargs.append(execution.input_file(params.get("cifti_in")))
    cargs.append(params.get("cifti_out"))
    if params.get("opt_mem_limit_limit_gb") is not None:
        cargs.extend([
            "-mem-limit",
            str(params.get("opt_mem_limit_limit_gb"))
        ])
    return cargs


def cifti_transpose_outputs(
    params: CiftiTransposeParameters,
    execution: Execution,
) -> CiftiTransposeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiTransposeOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_transpose_execute(
    params: CiftiTransposeParameters,
    execution: Execution,
) -> CiftiTransposeOutputs:
    """
    Transpose a cifti file.
    
    The input must be a 2-dimensional cifti file. The output is a cifti file
    where every row in the input is a column in the output.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiTransposeOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_transpose_cargs(params, execution)
    ret = cifti_transpose_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_transpose(
    cifti_in: InputPathType,
    cifti_out: str,
    opt_mem_limit_limit_gb: float | None = None,
    runner: Runner | None = None,
) -> CiftiTransposeOutputs:
    """
    Transpose a cifti file.
    
    The input must be a 2-dimensional cifti file. The output is a cifti file
    where every row in the input is a column in the output.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: the input cifti file.
        cifti_out: the output cifti file.
        opt_mem_limit_limit_gb: restrict memory usage: memory limit in\
            gigabytes.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiTransposeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_TRANSPOSE_METADATA)
    params = cifti_transpose_params(
        cifti_in=cifti_in,
        cifti_out=cifti_out,
        opt_mem_limit_limit_gb=opt_mem_limit_limit_gb,
    )
    return cifti_transpose_execute(params, execution)


__all__ = [
    "CIFTI_TRANSPOSE_METADATA",
    "CiftiTransposeOutputs",
    "CiftiTransposeParameters",
    "cifti_transpose",
    "cifti_transpose_params",
]
