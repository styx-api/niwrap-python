# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TBSS_4_PRESTATS_METADATA = Metadata(
    id="c3282aef88c580ce9e51953bf80329516d78b6be.boutiques",
    name="tbss_4_prestats",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


Tbss4PrestatsParameters = typing.TypedDict('Tbss4PrestatsParameters', {
    "__STYXTYPE__": typing.Literal["tbss_4_prestats"],
    "threshold": float,
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
        "tbss_4_prestats": tbss_4_prestats_cargs,
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


class Tbss4PrestatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_4_prestats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tbss_4_prestats_params(
    threshold: float = 0.2,
) -> Tbss4PrestatsParameters:
    """
    Build parameters.
    
    Args:
        threshold: Thresholding value for the Mean FA Skeleton; recommended\
            value is 0.2.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tbss_4_prestats",
        "threshold": threshold,
    }
    return params


def tbss_4_prestats_cargs(
    params: Tbss4PrestatsParameters,
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
    cargs.append("tbss_4_prestats")
    cargs.append(str(params.get("threshold")))
    return cargs


def tbss_4_prestats_outputs(
    params: Tbss4PrestatsParameters,
    execution: Execution,
) -> Tbss4PrestatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Tbss4PrestatsOutputs(
        root=execution.output_file("."),
    )
    return ret


def tbss_4_prestats_execute(
    params: Tbss4PrestatsParameters,
    execution: Execution,
) -> Tbss4PrestatsOutputs:
    """
    A tool for thresholding the Mean FA Skeleton in TBSS analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Tbss4PrestatsOutputs`).
    """
    params = execution.params(params)
    cargs = tbss_4_prestats_cargs(params, execution)
    ret = tbss_4_prestats_outputs(params, execution)
    execution.run(cargs)
    return ret


def tbss_4_prestats(
    threshold: float = 0.2,
    runner: Runner | None = None,
) -> Tbss4PrestatsOutputs:
    """
    A tool for thresholding the Mean FA Skeleton in TBSS analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        threshold: Thresholding value for the Mean FA Skeleton; recommended\
            value is 0.2.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tbss4PrestatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TBSS_4_PRESTATS_METADATA)
    params = tbss_4_prestats_params(
        threshold=threshold,
    )
    return tbss_4_prestats_execute(params, execution)


__all__ = [
    "TBSS_4_PRESTATS_METADATA",
    "Tbss4PrestatsOutputs",
    "Tbss4PrestatsParameters",
    "tbss_4_prestats",
    "tbss_4_prestats_params",
]
