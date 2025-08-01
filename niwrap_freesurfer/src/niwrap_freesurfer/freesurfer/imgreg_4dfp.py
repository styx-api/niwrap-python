# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

IMGREG_4DFP_METADATA = Metadata(
    id="56f755f16ccfb6ca990d0bdefae3bf38a4194227.boutiques",
    name="imgreg_4dfp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Imgreg4dfpParameters = typing.TypedDict('Imgreg4dfpParameters', {
    "__STYXTYPE__": typing.Literal["imgreg_4dfp"],
    "target_image": InputPathType,
    "target_mask": str,
    "source_image": InputPathType,
    "source_mask": str,
    "t4file": str,
    "mode": str,
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
        "imgreg_4dfp": imgreg_4dfp_cargs,
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


class Imgreg4dfpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imgreg_4dfp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def imgreg_4dfp_params(
    target_image: InputPathType,
    source_image: InputPathType,
    t4file: str,
    mode: str,
    target_mask: str = "none",
    source_mask: str = "none",
) -> Imgreg4dfpParameters:
    """
    Build parameters.
    
    Args:
        target_image: Target image.
        source_image: Source image.
        t4file: Transformation file.
        mode: Mode of operation.
        target_mask: Target mask.
        source_mask: Source mask.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "imgreg_4dfp",
        "target_image": target_image,
        "target_mask": target_mask,
        "source_image": source_image,
        "source_mask": source_mask,
        "t4file": t4file,
        "mode": mode,
    }
    return params


def imgreg_4dfp_cargs(
    params: Imgreg4dfpParameters,
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
    cargs.append("imgreg_4dfp")
    cargs.append(execution.input_file(params.get("target_image")))
    cargs.append(params.get("target_mask"))
    cargs.append(execution.input_file(params.get("source_image")))
    cargs.append(params.get("source_mask"))
    cargs.append(params.get("t4file"))
    cargs.append(params.get("mode"))
    return cargs


def imgreg_4dfp_outputs(
    params: Imgreg4dfpParameters,
    execution: Execution,
) -> Imgreg4dfpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Imgreg4dfpOutputs(
        root=execution.output_file("."),
    )
    return ret


def imgreg_4dfp_execute(
    params: Imgreg4dfpParameters,
    execution: Execution,
) -> Imgreg4dfpOutputs:
    """
    Image registration utility using 4dfp.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Imgreg4dfpOutputs`).
    """
    params = execution.params(params)
    cargs = imgreg_4dfp_cargs(params, execution)
    ret = imgreg_4dfp_outputs(params, execution)
    execution.run(cargs)
    return ret


def imgreg_4dfp(
    target_image: InputPathType,
    source_image: InputPathType,
    t4file: str,
    mode: str,
    target_mask: str = "none",
    source_mask: str = "none",
    runner: Runner | None = None,
) -> Imgreg4dfpOutputs:
    """
    Image registration utility using 4dfp.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        target_image: Target image.
        source_image: Source image.
        t4file: Transformation file.
        mode: Mode of operation.
        target_mask: Target mask.
        source_mask: Source mask.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Imgreg4dfpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMGREG_4DFP_METADATA)
    params = imgreg_4dfp_params(
        target_image=target_image,
        target_mask=target_mask,
        source_image=source_image,
        source_mask=source_mask,
        t4file=t4file,
        mode=mode,
    )
    return imgreg_4dfp_execute(params, execution)


__all__ = [
    "IMGREG_4DFP_METADATA",
    "Imgreg4dfpOutputs",
    "Imgreg4dfpParameters",
    "imgreg_4dfp",
    "imgreg_4dfp_params",
]
