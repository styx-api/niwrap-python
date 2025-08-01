# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ADJUNCT_TORT_PLOT_DP_ALIGN_METADATA = Metadata(
    id="476f4d1a86214009b6eb0878d5070c11cd6a6a27.boutiques",
    name="adjunct_tort_plot_dp_align",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


AdjunctTortPlotDpAlignParameters = typing.TypedDict('AdjunctTortPlotDpAlignParameters', {
    "__STYXTYPE__": typing.Literal["adjunct_tort_plot_dp_align"],
    "input_file": InputPathType,
    "output_prefix": str,
    "enorm_max": typing.NotRequired[float | None],
    "enorm_hline": typing.NotRequired[float | None],
    "no_svg": bool,
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
        "adjunct_tort_plot_dp_align": adjunct_tort_plot_dp_align_cargs,
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
        "adjunct_tort_plot_dp_align": adjunct_tort_plot_dp_align_outputs,
    }.get(t)


class AdjunctTortPlotDpAlignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_tort_plot_dp_align(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    align_params: OutputPathType
    """Text file containing 6 columns of data for the rigid-body alignment
    parameters estimated by DIFFPREP."""
    enorm_file: OutputPathType
    """Text file with 1 column of data, the Euclidean norm of the differences of
    the rigid body alignment parameters."""
    plot_jpg: OutputPathType
    """A plot of enorm and the alignment parameters in JPG format."""
    plot_svg: OutputPathType
    """A plot of enorm and the alignment parameters in SVG format."""


def adjunct_tort_plot_dp_align_params(
    input_file: InputPathType,
    output_prefix: str,
    enorm_max: float | None = None,
    enorm_hline: float | None = None,
    no_svg: bool = False,
) -> AdjunctTortPlotDpAlignParameters:
    """
    Build parameters.
    
    Args:
        input_file: Name of DIFFPREP-produced file to parse, probably ending in\
            '_transformations.txt'.
        output_prefix: Base of output files; can contain path information.\
            Should *not* include any extension.
        enorm_max: Specify max value of y-axis of enorm plot in SVG image.\
            Useful for having a constant value across a study.
        enorm_hline: Specify value of a horizontal, dotted, bright cyan line\
            for the enorm plot in SVG image. Can help with visualization.
        no_svg: Opt to turn off even checking to plot an SVG version of the\
            figure.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "adjunct_tort_plot_dp_align",
        "input_file": input_file,
        "output_prefix": output_prefix,
        "no_svg": no_svg,
    }
    if enorm_max is not None:
        params["enorm_max"] = enorm_max
    if enorm_hline is not None:
        params["enorm_hline"] = enorm_hline
    return params


def adjunct_tort_plot_dp_align_cargs(
    params: AdjunctTortPlotDpAlignParameters,
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
    cargs.append("adjunct_tort_plot_dp_align")
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-prefix",
        params.get("output_prefix")
    ])
    if params.get("enorm_max") is not None:
        cargs.extend([
            "-enorm_max",
            str(params.get("enorm_max"))
        ])
    if params.get("enorm_hline") is not None:
        cargs.extend([
            "-enorm_hline",
            str(params.get("enorm_hline"))
        ])
    if params.get("no_svg"):
        cargs.append("-no_svg")
    return cargs


def adjunct_tort_plot_dp_align_outputs(
    params: AdjunctTortPlotDpAlignParameters,
    execution: Execution,
) -> AdjunctTortPlotDpAlignOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AdjunctTortPlotDpAlignOutputs(
        root=execution.output_file("."),
        align_params=execution.output_file(params.get("output_prefix") + "_align.1D"),
        enorm_file=execution.output_file(params.get("output_prefix") + "_enorm.1D"),
        plot_jpg=execution.output_file(params.get("output_prefix") + ".jpg"),
        plot_svg=execution.output_file(params.get("output_prefix") + ".svg"),
    )
    return ret


def adjunct_tort_plot_dp_align_execute(
    params: AdjunctTortPlotDpAlignParameters,
    execution: Execution,
) -> AdjunctTortPlotDpAlignOutputs:
    """
    Tool to display the rigid-body alignment parameters from TORTOISE's DIFFPREP,
    useful for analyzing subject motion in DWI data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AdjunctTortPlotDpAlignOutputs`).
    """
    params = execution.params(params)
    cargs = adjunct_tort_plot_dp_align_cargs(params, execution)
    ret = adjunct_tort_plot_dp_align_outputs(params, execution)
    execution.run(cargs)
    return ret


def adjunct_tort_plot_dp_align(
    input_file: InputPathType,
    output_prefix: str,
    enorm_max: float | None = None,
    enorm_hline: float | None = None,
    no_svg: bool = False,
    runner: Runner | None = None,
) -> AdjunctTortPlotDpAlignOutputs:
    """
    Tool to display the rigid-body alignment parameters from TORTOISE's DIFFPREP,
    useful for analyzing subject motion in DWI data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Name of DIFFPREP-produced file to parse, probably ending in\
            '_transformations.txt'.
        output_prefix: Base of output files; can contain path information.\
            Should *not* include any extension.
        enorm_max: Specify max value of y-axis of enorm plot in SVG image.\
            Useful for having a constant value across a study.
        enorm_hline: Specify value of a horizontal, dotted, bright cyan line\
            for the enorm plot in SVG image. Can help with visualization.
        no_svg: Opt to turn off even checking to plot an SVG version of the\
            figure.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctTortPlotDpAlignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_TORT_PLOT_DP_ALIGN_METADATA)
    params = adjunct_tort_plot_dp_align_params(
        input_file=input_file,
        output_prefix=output_prefix,
        enorm_max=enorm_max,
        enorm_hline=enorm_hline,
        no_svg=no_svg,
    )
    return adjunct_tort_plot_dp_align_execute(params, execution)


__all__ = [
    "ADJUNCT_TORT_PLOT_DP_ALIGN_METADATA",
    "AdjunctTortPlotDpAlignOutputs",
    "AdjunctTortPlotDpAlignParameters",
    "adjunct_tort_plot_dp_align",
    "adjunct_tort_plot_dp_align_params",
]
