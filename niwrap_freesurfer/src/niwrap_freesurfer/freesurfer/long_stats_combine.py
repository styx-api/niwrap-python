# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LONG_STATS_COMBINE_METADATA = Metadata(
    id="bc07fa2d21f0070237805d7567bf0841a65a42f5.boutiques",
    name="long_stats_combine",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


LongStatsCombineParameters = typing.TypedDict('LongStatsCombineParameters', {
    "__STYX_TYPE__": typing.Literal["long_stats_combine"],
    "qdec": InputPathType,
    "stats": str,
    "measure": str,
    "subject_dir": str,
    "output_qdec": str,
    "output_stats": typing.NotRequired[str | None],
    "input_stats": typing.NotRequired[InputPathType | None],
    "cross_sectional": bool,
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
        "long_stats_combine": long_stats_combine_cargs,
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
        "long_stats_combine": long_stats_combine_outputs,
    }.get(t)


class LongStatsCombineOutputs(typing.NamedTuple):
    """
    Output object returned when calling `long_stats_combine(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_qdec_file: OutputPathType
    """Output long qdec table"""
    output_stacked_stats_file: OutputPathType | None
    """Stacked stats table for all subjects, all time points"""


def long_stats_combine_params(
    qdec: InputPathType,
    stats: str,
    measure: str,
    subject_dir: str,
    output_qdec: str,
    output_stats: str | None = None,
    input_stats: InputPathType | None = None,
    cross_sectional: bool = False,
) -> LongStatsCombineParameters:
    """
    Build parameters.
    
    Args:
        qdec: QDEC table file specifying the subjects and time points. File has\
            first columns: fsid fsid-base.
        stats: The stats file, e.g. aseg.stats or lh.aparc.stats.
        measure: The stats measure (e.g. volume, thickness, mean, std).
        subject_dir: Full path to FreeSurfer subjects directory.
        output_qdec: File name of output long qdec table.
        output_stats: File name to output stacked stats table (all subjects,\
            all time points).
        input_stats: File name of stacked stats table (same order as qdec),\
            instead of using --stats and --meas.
        cross_sectional: Use cross sectional results (for testing only).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "long_stats_combine",
        "qdec": qdec,
        "stats": stats,
        "measure": measure,
        "subject_dir": subject_dir,
        "output_qdec": output_qdec,
        "cross_sectional": cross_sectional,
    }
    if output_stats is not None:
        params["output_stats"] = output_stats
    if input_stats is not None:
        params["input_stats"] = input_stats
    return params


def long_stats_combine_cargs(
    params: LongStatsCombineParameters,
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
    cargs.append("long_stats_combine")
    cargs.extend([
        "--qdec",
        execution.input_file(params.get("qdec"))
    ])
    cargs.extend([
        "--stats",
        params.get("stats")
    ])
    cargs.extend([
        "--meas",
        params.get("measure")
    ])
    cargs.extend([
        "--sd",
        params.get("subject_dir")
    ])
    cargs.extend([
        "--outqdec",
        params.get("output_qdec")
    ])
    if params.get("output_stats") is not None:
        cargs.extend([
            "--outstats",
            params.get("output_stats")
        ])
    if params.get("input_stats") is not None:
        cargs.extend([
            "--instats",
            execution.input_file(params.get("input_stats"))
        ])
    if params.get("cross_sectional"):
        cargs.append("--cross")
    return cargs


def long_stats_combine_outputs(
    params: LongStatsCombineParameters,
    execution: Execution,
) -> LongStatsCombineOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = LongStatsCombineOutputs(
        root=execution.output_file("."),
        output_qdec_file=execution.output_file(params.get("output_qdec")),
        output_stacked_stats_file=execution.output_file(params.get("output_stats")) if (params.get("output_stats") is not None) else None,
    )
    return ret


def long_stats_combine_execute(
    params: LongStatsCombineParameters,
    execution: Execution,
) -> LongStatsCombineOutputs:
    """
    Adds columns from stats into longitudinal qdec table, using longitudinally
    processed results.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `LongStatsCombineOutputs`).
    """
    params = execution.params(params)
    cargs = long_stats_combine_cargs(params, execution)
    ret = long_stats_combine_outputs(params, execution)
    execution.run(cargs)
    return ret


def long_stats_combine(
    qdec: InputPathType,
    stats: str,
    measure: str,
    subject_dir: str,
    output_qdec: str,
    output_stats: str | None = None,
    input_stats: InputPathType | None = None,
    cross_sectional: bool = False,
    runner: Runner | None = None,
) -> LongStatsCombineOutputs:
    """
    Adds columns from stats into longitudinal qdec table, using longitudinally
    processed results.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        qdec: QDEC table file specifying the subjects and time points. File has\
            first columns: fsid fsid-base.
        stats: The stats file, e.g. aseg.stats or lh.aparc.stats.
        measure: The stats measure (e.g. volume, thickness, mean, std).
        subject_dir: Full path to FreeSurfer subjects directory.
        output_qdec: File name of output long qdec table.
        output_stats: File name to output stacked stats table (all subjects,\
            all time points).
        input_stats: File name of stacked stats table (same order as qdec),\
            instead of using --stats and --meas.
        cross_sectional: Use cross sectional results (for testing only).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LongStatsCombineOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LONG_STATS_COMBINE_METADATA)
    params = long_stats_combine_params(
        qdec=qdec,
        stats=stats,
        measure=measure,
        subject_dir=subject_dir,
        output_qdec=output_qdec,
        output_stats=output_stats,
        input_stats=input_stats,
        cross_sectional=cross_sectional,
    )
    return long_stats_combine_execute(params, execution)


__all__ = [
    "LONG_STATS_COMBINE_METADATA",
    "LongStatsCombineOutputs",
    "LongStatsCombineParameters",
    "long_stats_combine",
    "long_stats_combine_params",
]
