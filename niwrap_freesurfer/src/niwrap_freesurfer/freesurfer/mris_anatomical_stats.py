# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_ANATOMICAL_STATS_METADATA = Metadata(
    id="117a911cbb95d3ef62e62e40a756554d2c622c20.boutiques",
    name="mris_anatomical_stats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisAnatomicalStatsParameters = typing.TypedDict('MrisAnatomicalStatsParameters', {
    "__STYXTYPE__": typing.Literal["mris_anatomical_stats"],
    "subjectname": str,
    "hemisphere": str,
    "surfacename": typing.NotRequired[str | None],
    "thickness_range": typing.NotRequired[list[float] | None],
    "label_file": typing.NotRequired[InputPathType | None],
    "thickness_file": typing.NotRequired[InputPathType | None],
    "annotation_file": typing.NotRequired[InputPathType | None],
    "tabular_output": bool,
    "tablefile": typing.NotRequired[str | None],
    "logfile": typing.NotRequired[str | None],
    "nsmooth": typing.NotRequired[float | None],
    "color_table": typing.NotRequired[str | None],
    "noglobal": bool,
    "th3_computation": bool,
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
        "mris_anatomical_stats": mris_anatomical_stats_cargs,
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
        "mris_anatomical_stats": mris_anatomical_stats_outputs,
    }.get(t)


class MrisAnatomicalStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_anatomical_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_log_file: OutputPathType | None
    """Output log file of the statistics"""
    output_table_file: OutputPathType | None
    """Tabular output stored in a table file"""
    output_ctab_file: OutputPathType | None
    """Output annotation color table file"""


def mris_anatomical_stats_params(
    subjectname: str,
    hemisphere: str,
    surfacename: str | None = None,
    thickness_range: list[float] | None = None,
    label_file: InputPathType | None = None,
    thickness_file: InputPathType | None = None,
    annotation_file: InputPathType | None = None,
    tabular_output: bool = False,
    tablefile: str | None = None,
    logfile: str | None = None,
    nsmooth: float | None = None,
    color_table: str | None = None,
    noglobal: bool = False,
    th3_computation: bool = False,
) -> MrisAnatomicalStatsParameters:
    """
    Build parameters.
    
    Args:
        subjectname: Subject name.
        hemisphere: Hemisphere.
        surfacename: Surface name.
        thickness_range: Only consider thicknesses in the specified range.
        label_file: Limit calculations to specified label.
        thickness_file: Use specified file for computing thickness statistics.
        annotation_file: Compute properties for each label in the annotation\
            file separately.
        tabular_output: Tabular output.
        tablefile: Table output to tablefile. Must use -a or -l options to\
            specify input.
        logfile: Write stats to file named log.
        nsmooth: Smooth thickness map # of iterations before using it.
        color_table: Output annotation file's color table to text file.
        noglobal: Do not compute global brain stats.
        th3_computation: Compute vertex-wise volume by dividing each obliquely\
            truncated trilateral pyramid into three tetrahedra.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_anatomical_stats",
        "subjectname": subjectname,
        "hemisphere": hemisphere,
        "tabular_output": tabular_output,
        "noglobal": noglobal,
        "th3_computation": th3_computation,
    }
    if surfacename is not None:
        params["surfacename"] = surfacename
    if thickness_range is not None:
        params["thickness_range"] = thickness_range
    if label_file is not None:
        params["label_file"] = label_file
    if thickness_file is not None:
        params["thickness_file"] = thickness_file
    if annotation_file is not None:
        params["annotation_file"] = annotation_file
    if tablefile is not None:
        params["tablefile"] = tablefile
    if logfile is not None:
        params["logfile"] = logfile
    if nsmooth is not None:
        params["nsmooth"] = nsmooth
    if color_table is not None:
        params["color_table"] = color_table
    return params


def mris_anatomical_stats_cargs(
    params: MrisAnatomicalStatsParameters,
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
    cargs.append("mris_anatomical_stats")
    cargs.append(params.get("subjectname"))
    cargs.append(params.get("hemisphere"))
    if params.get("surfacename") is not None:
        cargs.append(params.get("surfacename"))
    if params.get("thickness_range") is not None:
        cargs.extend([
            "-i",
            *map(str, params.get("thickness_range"))
        ])
    if params.get("label_file") is not None:
        cargs.extend([
            "-l",
            execution.input_file(params.get("label_file"))
        ])
    if params.get("thickness_file") is not None:
        cargs.extend([
            "-t",
            execution.input_file(params.get("thickness_file"))
        ])
    if params.get("annotation_file") is not None:
        cargs.extend([
            "-a",
            execution.input_file(params.get("annotation_file"))
        ])
    if params.get("tabular_output"):
        cargs.append("-b")
    if params.get("tablefile") is not None:
        cargs.extend([
            "-f",
            params.get("tablefile")
        ])
    if params.get("logfile") is not None:
        cargs.extend([
            "-log",
            params.get("logfile")
        ])
    if params.get("nsmooth") is not None:
        cargs.extend([
            "-nsmooth",
            str(params.get("nsmooth"))
        ])
    if params.get("color_table") is not None:
        cargs.extend([
            "-c",
            params.get("color_table")
        ])
    if params.get("noglobal"):
        cargs.append("-noglobal")
    if params.get("th3_computation"):
        cargs.append("-th3")
    return cargs


def mris_anatomical_stats_outputs(
    params: MrisAnatomicalStatsParameters,
    execution: Execution,
) -> MrisAnatomicalStatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisAnatomicalStatsOutputs(
        root=execution.output_file("."),
        output_log_file=execution.output_file(params.get("logfile") + ".txt") if (params.get("logfile") is not None) else None,
        output_table_file=execution.output_file(params.get("tablefile") + ".txt") if (params.get("tablefile") is not None) else None,
        output_ctab_file=execution.output_file(params.get("color_table") + ".txt") if (params.get("color_table") is not None) else None,
    )
    return ret


def mris_anatomical_stats_execute(
    params: MrisAnatomicalStatsParameters,
    execution: Execution,
) -> MrisAnatomicalStatsOutputs:
    """
    This program computes a number of anatomical properties.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisAnatomicalStatsOutputs`).
    """
    params = execution.params(params)
    cargs = mris_anatomical_stats_cargs(params, execution)
    ret = mris_anatomical_stats_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_anatomical_stats(
    subjectname: str,
    hemisphere: str,
    surfacename: str | None = None,
    thickness_range: list[float] | None = None,
    label_file: InputPathType | None = None,
    thickness_file: InputPathType | None = None,
    annotation_file: InputPathType | None = None,
    tabular_output: bool = False,
    tablefile: str | None = None,
    logfile: str | None = None,
    nsmooth: float | None = None,
    color_table: str | None = None,
    noglobal: bool = False,
    th3_computation: bool = False,
    runner: Runner | None = None,
) -> MrisAnatomicalStatsOutputs:
    """
    This program computes a number of anatomical properties.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjectname: Subject name.
        hemisphere: Hemisphere.
        surfacename: Surface name.
        thickness_range: Only consider thicknesses in the specified range.
        label_file: Limit calculations to specified label.
        thickness_file: Use specified file for computing thickness statistics.
        annotation_file: Compute properties for each label in the annotation\
            file separately.
        tabular_output: Tabular output.
        tablefile: Table output to tablefile. Must use -a or -l options to\
            specify input.
        logfile: Write stats to file named log.
        nsmooth: Smooth thickness map # of iterations before using it.
        color_table: Output annotation file's color table to text file.
        noglobal: Do not compute global brain stats.
        th3_computation: Compute vertex-wise volume by dividing each obliquely\
            truncated trilateral pyramid into three tetrahedra.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisAnatomicalStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_ANATOMICAL_STATS_METADATA)
    params = mris_anatomical_stats_params(
        subjectname=subjectname,
        hemisphere=hemisphere,
        surfacename=surfacename,
        thickness_range=thickness_range,
        label_file=label_file,
        thickness_file=thickness_file,
        annotation_file=annotation_file,
        tabular_output=tabular_output,
        tablefile=tablefile,
        logfile=logfile,
        nsmooth=nsmooth,
        color_table=color_table,
        noglobal=noglobal,
        th3_computation=th3_computation,
    )
    return mris_anatomical_stats_execute(params, execution)


__all__ = [
    "MRIS_ANATOMICAL_STATS_METADATA",
    "MrisAnatomicalStatsOutputs",
    "MrisAnatomicalStatsParameters",
    "mris_anatomical_stats",
    "mris_anatomical_stats_params",
]
