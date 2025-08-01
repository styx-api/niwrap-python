# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DMRI_STATS_AC_METADATA = Metadata(
    id="21231274d559cc0139f162ed232ad7163aa93c8f.boutiques",
    name="dmri_stats_ac",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


DmriStatsAcParameters = typing.TypedDict('DmriStatsAcParameters', {
    "__STYXTYPE__": typing.Literal["dmri_stats_ac"],
    "anatomicuts_folder": str,
    "num_clusters": int,
    "correspondence_file": str,
    "measures": list[str],
    "output_file": str,
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
        "dmri_stats_ac": dmri_stats_ac_cargs,
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
        "dmri_stats_ac": dmri_stats_ac_outputs,
    }.get(t)


class DmriStatsAcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_stats_ac(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output of the dMRI statistical analysis"""


def dmri_stats_ac_params(
    anatomicuts_folder: str,
    num_clusters: int,
    correspondence_file: str,
    measures: list[str],
    output_file: str,
) -> DmriStatsAcParameters:
    """
    Build parameters.
    
    Args:
        anatomicuts_folder: Input folder containing anatomicuts data.
        num_clusters: Number of clusters for analysis.
        correspondence_file: File specifying correspondence details.
        measures: Number of measures followed by each measure name and file.
        output_file: Output file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_stats_ac",
        "anatomicuts_folder": anatomicuts_folder,
        "num_clusters": num_clusters,
        "correspondence_file": correspondence_file,
        "measures": measures,
        "output_file": output_file,
    }
    return params


def dmri_stats_ac_cargs(
    params: DmriStatsAcParameters,
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
    cargs.append("dmri_stats_ac")
    cargs.extend([
        "-i",
        params.get("anatomicuts_folder")
    ])
    cargs.extend([
        "-n",
        str(params.get("num_clusters"))
    ])
    cargs.extend([
        "-c",
        params.get("correspondence_file")
    ])
    cargs.extend([
        "-m",
        *params.get("measures")
    ])
    cargs.extend([
        "-o",
        params.get("output_file")
    ])
    return cargs


def dmri_stats_ac_outputs(
    params: DmriStatsAcParameters,
    execution: Execution,
) -> DmriStatsAcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriStatsAcOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_file")),
    )
    return ret


def dmri_stats_ac_execute(
    params: DmriStatsAcParameters,
    execution: Execution,
) -> DmriStatsAcOutputs:
    """
    The tool 'dmri_stats_ac' performs statistical analysis on dMRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriStatsAcOutputs`).
    """
    params = execution.params(params)
    cargs = dmri_stats_ac_cargs(params, execution)
    ret = dmri_stats_ac_outputs(params, execution)
    execution.run(cargs)
    return ret


def dmri_stats_ac(
    anatomicuts_folder: str,
    num_clusters: int,
    correspondence_file: str,
    measures: list[str],
    output_file: str,
    runner: Runner | None = None,
) -> DmriStatsAcOutputs:
    """
    The tool 'dmri_stats_ac' performs statistical analysis on dMRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        anatomicuts_folder: Input folder containing anatomicuts data.
        num_clusters: Number of clusters for analysis.
        correspondence_file: File specifying correspondence details.
        measures: Number of measures followed by each measure name and file.
        output_file: Output file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriStatsAcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_STATS_AC_METADATA)
    params = dmri_stats_ac_params(
        anatomicuts_folder=anatomicuts_folder,
        num_clusters=num_clusters,
        correspondence_file=correspondence_file,
        measures=measures,
        output_file=output_file,
    )
    return dmri_stats_ac_execute(params, execution)


__all__ = [
    "DMRI_STATS_AC_METADATA",
    "DmriStatsAcOutputs",
    "DmriStatsAcParameters",
    "dmri_stats_ac",
    "dmri_stats_ac_params",
]
