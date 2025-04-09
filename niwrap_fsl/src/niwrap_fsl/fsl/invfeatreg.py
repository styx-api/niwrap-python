# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

INVFEATREG_METADATA = Metadata(
    id="99bb1f8fb4e4e88660733aa203a1237143f95934.boutiques",
    name="invfeatreg",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


InvfeatregParameters = typing.TypedDict('InvfeatregParameters', {
    "__STYX_TYPE__": typing.Literal["invfeatreg"],
    "feat_directory": str,
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
        "invfeatreg": invfeatreg_cargs,
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
    }.get(t)


class InvfeatregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `invfeatreg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def invfeatreg_params(
    feat_directory: str,
) -> InvfeatregParameters:
    """
    Build parameters.
    
    Args:
        feat_directory: FEAT Directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "invfeatreg",
        "feat_directory": feat_directory,
    }
    return params


def invfeatreg_cargs(
    params: InvfeatregParameters,
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
    cargs.append("invfeatreg")
    cargs.append(params.get("feat_directory"))
    return cargs


def invfeatreg_outputs(
    params: InvfeatregParameters,
    execution: Execution,
) -> InvfeatregOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = InvfeatregOutputs(
        root=execution.output_file("."),
    )
    return ret


def invfeatreg_execute(
    params: InvfeatregParameters,
    execution: Execution,
) -> InvfeatregOutputs:
    """
    Inverse warp image using FNIRT.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `InvfeatregOutputs`).
    """
    params = execution.params(params)
    cargs = invfeatreg_cargs(params, execution)
    ret = invfeatreg_outputs(params, execution)
    execution.run(cargs)
    return ret


def invfeatreg(
    feat_directory: str,
    runner: Runner | None = None,
) -> InvfeatregOutputs:
    """
    Inverse warp image using FNIRT.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        feat_directory: FEAT Directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InvfeatregOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INVFEATREG_METADATA)
    params = invfeatreg_params(
        feat_directory=feat_directory,
    )
    return invfeatreg_execute(params, execution)


__all__ = [
    "INVFEATREG_METADATA",
    "InvfeatregOutputs",
    "InvfeatregParameters",
    "invfeatreg",
    "invfeatreg_params",
]
