# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_TSPLOT_METADATA = Metadata(
    id="4faf84b9675a1e313f3f8cf1864b39e81af5cf94.boutiques",
    name="fsl_tsplot",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslTsplotParameters = typing.TypedDict('FslTsplotParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_tsplot"],
    "input_files": str,
    "output_file": str,
    "title": typing.NotRequired[str | None],
    "legend_file": typing.NotRequired[str | None],
    "labels": typing.NotRequired[str | None],
    "ymin": typing.NotRequired[float | None],
    "ymax": typing.NotRequired[float | None],
    "xlabel": typing.NotRequired[str | None],
    "ylabel": typing.NotRequired[str | None],
    "height": typing.NotRequired[float | None],
    "width": typing.NotRequired[float | None],
    "unit": typing.NotRequired[float | None],
    "precision": typing.NotRequired[float | None],
    "sci_flag": bool,
    "start_col": typing.NotRequired[float | None],
    "end_col": typing.NotRequired[float | None],
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
        "fsl_tsplot": fsl_tsplot_cargs,
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
        "fsl_tsplot": fsl_tsplot_outputs,
    }.get(t)


class FslTsplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_tsplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_png: OutputPathType
    """Output PNG file"""


def fsl_tsplot_params(
    input_files: str,
    output_file: str,
    title: str | None = None,
    legend_file: str | None = None,
    labels: str | None = None,
    ymin: float | None = None,
    ymax: float | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    height: float | None = None,
    width: float | None = None,
    unit: float | None = None,
    precision: float | None = None,
    sci_flag: bool = False,
    start_col: float | None = None,
    end_col: float | None = None,
) -> FslTsplotParameters:
    """
    Build parameters.
    
    Args:
        input_files: Comma-separated list of input file names (ASCII text\
            matrix, one column per timecourse).
        output_file: Output filename for the PNG file.
        title: Plot title.
        legend_file: File name of ASCII text file, one row per legend entry.
        labels: Comma-separated list of labels.
        ymin: Minimum y-value.
        ymax: Maximum y-value.
        xlabel: X-axis label.
        ylabel: Y-axis label.
        height: Plot height in pixels (default 150).
        width: Plot width in pixels (default 600).
        unit: Scaling units for x-axis (default 1...length of infile).
        precision: Precision of x-axis labels.
        sci_flag: Switch on scientific notation.
        start_col: Position of first column to plot.
        end_col: Position of final column to plot.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_tsplot",
        "input_files": input_files,
        "output_file": output_file,
        "sci_flag": sci_flag,
    }
    if title is not None:
        params["title"] = title
    if legend_file is not None:
        params["legend_file"] = legend_file
    if labels is not None:
        params["labels"] = labels
    if ymin is not None:
        params["ymin"] = ymin
    if ymax is not None:
        params["ymax"] = ymax
    if xlabel is not None:
        params["xlabel"] = xlabel
    if ylabel is not None:
        params["ylabel"] = ylabel
    if height is not None:
        params["height"] = height
    if width is not None:
        params["width"] = width
    if unit is not None:
        params["unit"] = unit
    if precision is not None:
        params["precision"] = precision
    if start_col is not None:
        params["start_col"] = start_col
    if end_col is not None:
        params["end_col"] = end_col
    return params


def fsl_tsplot_cargs(
    params: FslTsplotParameters,
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
    cargs.append("fsl_tsplot")
    cargs.extend([
        "-i",
        params.get("input_files")
    ])
    cargs.extend([
        "-o",
        params.get("output_file")
    ])
    if params.get("title") is not None:
        cargs.extend([
            "-t",
            params.get("title")
        ])
    if params.get("legend_file") is not None:
        cargs.extend([
            "-l",
            params.get("legend_file")
        ])
    if params.get("labels") is not None:
        cargs.extend([
            "-a",
            params.get("labels")
        ])
    if params.get("ymin") is not None:
        cargs.extend([
            "--ymin",
            str(params.get("ymin"))
        ])
    if params.get("ymax") is not None:
        cargs.extend([
            "--ymax",
            str(params.get("ymax"))
        ])
    if params.get("xlabel") is not None:
        cargs.extend([
            "-x",
            params.get("xlabel")
        ])
    if params.get("ylabel") is not None:
        cargs.extend([
            "-y",
            params.get("ylabel")
        ])
    if params.get("height") is not None:
        cargs.extend([
            "-h",
            str(params.get("height"))
        ])
    if params.get("width") is not None:
        cargs.extend([
            "-w",
            str(params.get("width"))
        ])
    if params.get("unit") is not None:
        cargs.extend([
            "-u",
            str(params.get("unit"))
        ])
    if params.get("precision") is not None:
        cargs.extend([
            "--precision",
            str(params.get("precision"))
        ])
    if params.get("sci_flag"):
        cargs.append("--sci")
    if params.get("start_col") is not None:
        cargs.extend([
            "--start",
            str(params.get("start_col"))
        ])
    if params.get("end_col") is not None:
        cargs.extend([
            "--finish",
            str(params.get("end_col"))
        ])
    return cargs


def fsl_tsplot_outputs(
    params: FslTsplotParameters,
    execution: Execution,
) -> FslTsplotOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslTsplotOutputs(
        root=execution.output_file("."),
        output_png=execution.output_file(params.get("output_file")),
    )
    return ret


def fsl_tsplot_execute(
    params: FslTsplotParameters,
    execution: Execution,
) -> FslTsplotOutputs:
    """
    Timeseries plotting tool from FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslTsplotOutputs`).
    """
    params = execution.params(params)
    cargs = fsl_tsplot_cargs(params, execution)
    ret = fsl_tsplot_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_tsplot(
    input_files: str,
    output_file: str,
    title: str | None = None,
    legend_file: str | None = None,
    labels: str | None = None,
    ymin: float | None = None,
    ymax: float | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    height: float | None = None,
    width: float | None = None,
    unit: float | None = None,
    precision: float | None = None,
    sci_flag: bool = False,
    start_col: float | None = None,
    end_col: float | None = None,
    runner: Runner | None = None,
) -> FslTsplotOutputs:
    """
    Timeseries plotting tool from FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_files: Comma-separated list of input file names (ASCII text\
            matrix, one column per timecourse).
        output_file: Output filename for the PNG file.
        title: Plot title.
        legend_file: File name of ASCII text file, one row per legend entry.
        labels: Comma-separated list of labels.
        ymin: Minimum y-value.
        ymax: Maximum y-value.
        xlabel: X-axis label.
        ylabel: Y-axis label.
        height: Plot height in pixels (default 150).
        width: Plot width in pixels (default 600).
        unit: Scaling units for x-axis (default 1...length of infile).
        precision: Precision of x-axis labels.
        sci_flag: Switch on scientific notation.
        start_col: Position of first column to plot.
        end_col: Position of final column to plot.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslTsplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_TSPLOT_METADATA)
    params = fsl_tsplot_params(
        input_files=input_files,
        output_file=output_file,
        title=title,
        legend_file=legend_file,
        labels=labels,
        ymin=ymin,
        ymax=ymax,
        xlabel=xlabel,
        ylabel=ylabel,
        height=height,
        width=width,
        unit=unit,
        precision=precision,
        sci_flag=sci_flag,
        start_col=start_col,
        end_col=end_col,
    )
    return fsl_tsplot_execute(params, execution)


__all__ = [
    "FSL_TSPLOT_METADATA",
    "FslTsplotOutputs",
    "FslTsplotParameters",
    "fsl_tsplot",
    "fsl_tsplot_params",
]
