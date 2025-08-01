# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_MULTISCALE_STATS_METADATA = Metadata(
    id="70485123c5f0182ca6af11b7463e3a674edf9419.boutiques",
    name="mris_multiscale_stats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisMultiscaleStatsParameters = typing.TypedDict('MrisMultiscaleStatsParameters', {
    "__STYXTYPE__": typing.Literal["mris_multiscale_stats"],
    "output_subject": str,
    "hemi": str,
    "surf": InputPathType,
    "curv": InputPathType,
    "class1_subjects": list[str],
    "class2_subjects": list[str],
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
        "mris_multiscale_stats": mris_multiscale_stats_cargs,
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


class MrisMultiscaleStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_multiscale_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_multiscale_stats_params(
    output_subject: str,
    hemi: str,
    surf: InputPathType,
    curv: InputPathType,
    class1_subjects: list[str],
    class2_subjects: list[str],
) -> MrisMultiscaleStatsParameters:
    """
    Build parameters.
    
    Args:
        output_subject: The output subject identifier.
        hemi: Specify which hemisphere to use.
        surf: A spherical surface file suitable for computing geodesics.
        curv: The curvature file to be processed.
        class1_subjects: List of subjects from one class.
        class2_subjects: List of subjects from another class.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_multiscale_stats",
        "output_subject": output_subject,
        "hemi": hemi,
        "surf": surf,
        "curv": curv,
        "class1_subjects": class1_subjects,
        "class2_subjects": class2_subjects,
    }
    return params


def mris_multiscale_stats_cargs(
    params: MrisMultiscaleStatsParameters,
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
    cargs.append("mris_multiscale_stats")
    cargs.extend([
        "-o",
        params.get("output_subject")
    ])
    cargs.append(params.get("hemi"))
    cargs.append(execution.input_file(params.get("surf")))
    cargs.append(execution.input_file(params.get("curv")))
    cargs.extend(params.get("class1_subjects"))
    cargs.extend(params.get("class2_subjects"))
    return cargs


def mris_multiscale_stats_outputs(
    params: MrisMultiscaleStatsParameters,
    execution: Execution,
) -> MrisMultiscaleStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisMultiscaleStatsOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_multiscale_stats_execute(
    params: MrisMultiscaleStatsParameters,
    execution: Execution,
) -> MrisMultiscaleStatsOutputs:
    """
    Compute the autocorrelation function of a curvature file using multiscale
    statistical techniques.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisMultiscaleStatsOutputs`).
    """
    params = execution.params(params)
    cargs = mris_multiscale_stats_cargs(params, execution)
    ret = mris_multiscale_stats_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_multiscale_stats(
    output_subject: str,
    hemi: str,
    surf: InputPathType,
    curv: InputPathType,
    class1_subjects: list[str],
    class2_subjects: list[str],
    runner: Runner | None = None,
) -> MrisMultiscaleStatsOutputs:
    """
    Compute the autocorrelation function of a curvature file using multiscale
    statistical techniques.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_subject: The output subject identifier.
        hemi: Specify which hemisphere to use.
        surf: A spherical surface file suitable for computing geodesics.
        curv: The curvature file to be processed.
        class1_subjects: List of subjects from one class.
        class2_subjects: List of subjects from another class.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMultiscaleStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MULTISCALE_STATS_METADATA)
    params = mris_multiscale_stats_params(
        output_subject=output_subject,
        hemi=hemi,
        surf=surf,
        curv=curv,
        class1_subjects=class1_subjects,
        class2_subjects=class2_subjects,
    )
    return mris_multiscale_stats_execute(params, execution)


__all__ = [
    "MRIS_MULTISCALE_STATS_METADATA",
    "MrisMultiscaleStatsOutputs",
    "MrisMultiscaleStatsParameters",
    "mris_multiscale_stats",
    "mris_multiscale_stats_params",
]
