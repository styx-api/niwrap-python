# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SPM_T_TO_B_METADATA = Metadata(
    id="aeb4cbf77424f7a4691e003e7bad0ef280a42842.boutiques",
    name="spm_t_to_b",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


SpmTToBParameters = typing.TypedDict('SpmTToBParameters', {
    "__STYX_TYPE__": typing.Literal["spm_t_to_b"],
    "spm_stem_format": str,
    "bshort_stem": str,
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
        "spm_t_to_b": spm_t_to_b_cargs,
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


class SpmTToBOutputs(typing.NamedTuple):
    """
    Output object returned when calling `spm_t_to_b(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def spm_t_to_b_params(
    spm_stem_format: str,
    bshort_stem: str,
) -> SpmTToBParameters:
    """
    Build parameters.
    
    Args:
        spm_stem_format: Input SPM stem format.
        bshort_stem: Output bshort stem.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "spm_t_to_b",
        "spm_stem_format": spm_stem_format,
        "bshort_stem": bshort_stem,
    }
    return params


def spm_t_to_b_cargs(
    params: SpmTToBParameters,
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
    cargs.append("spm_t_to_b")
    cargs.append(params.get("spm_stem_format"))
    cargs.append(params.get("bshort_stem"))
    return cargs


def spm_t_to_b_outputs(
    params: SpmTToBParameters,
    execution: Execution,
) -> SpmTToBOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SpmTToBOutputs(
        root=execution.output_file("."),
    )
    return ret


def spm_t_to_b_execute(
    params: SpmTToBParameters,
    execution: Execution,
) -> SpmTToBOutputs:
    """
    Converts SPM format to Bshort format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SpmTToBOutputs`).
    """
    params = execution.params(params)
    cargs = spm_t_to_b_cargs(params, execution)
    ret = spm_t_to_b_outputs(params, execution)
    execution.run(cargs)
    return ret


def spm_t_to_b(
    spm_stem_format: str,
    bshort_stem: str,
    runner: Runner | None = None,
) -> SpmTToBOutputs:
    """
    Converts SPM format to Bshort format.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        spm_stem_format: Input SPM stem format.
        bshort_stem: Output bshort stem.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SpmTToBOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPM_T_TO_B_METADATA)
    params = spm_t_to_b_params(
        spm_stem_format=spm_stem_format,
        bshort_stem=bshort_stem,
    )
    return spm_t_to_b_execute(params, execution)


__all__ = [
    "SPM_T_TO_B_METADATA",
    "SpmTToBOutputs",
    "SpmTToBParameters",
    "spm_t_to_b",
    "spm_t_to_b_params",
]
