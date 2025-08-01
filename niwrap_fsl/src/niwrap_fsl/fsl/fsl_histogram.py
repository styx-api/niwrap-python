# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_HISTOGRAM_METADATA = Metadata(
    id="297d2f3bd8505222537d6ca114791495dc326caa.boutiques",
    name="fsl_histogram",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslHistogramParameters = typing.TypedDict('FslHistogramParameters', {
    "__STYXTYPE__": typing.Literal["fsl_histogram"],
    "input_file": InputPathType,
    "input_file_duplicate": InputPathType,
    "output_file": str,
    "output_file_duplicate": str,
    "mask_file": typing.NotRequired[InputPathType | None],
    "mask_file_duplicate": typing.NotRequired[InputPathType | None],
    "gmmfit_file": typing.NotRequired[InputPathType | None],
    "gmmfit_file_duplicate": typing.NotRequired[InputPathType | None],
    "plot_title": typing.NotRequired[str | None],
    "plot_title_duplicate": typing.NotRequired[str | None],
    "legend_file": typing.NotRequired[InputPathType | None],
    "legend_file_duplicate": typing.NotRequired[InputPathType | None],
    "xlabel": typing.NotRequired[str | None],
    "xlabel_duplicate": typing.NotRequired[str | None],
    "ylabel": typing.NotRequired[str | None],
    "ylabel_duplicate": typing.NotRequired[str | None],
    "plot_height": typing.NotRequired[float | None],
    "plot_height_duplicate": typing.NotRequired[float | None],
    "plot_width": typing.NotRequired[float | None],
    "plot_width_duplicate": typing.NotRequired[float | None],
    "num_bins": typing.NotRequired[float | None],
    "num_bins_duplicate": typing.NotRequired[float | None],
    "zoom_factor": typing.NotRequired[float | None],
    "zoom_factor_duplicate": typing.NotRequired[float | None],
    "use_gmm_flag": bool,
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
        "fsl_histogram": fsl_histogram_cargs,
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
        "fsl_histogram": fsl_histogram_outputs,
    }.get(t)


class FslHistogramOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_histogram(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    png_file: OutputPathType
    """Generated PNG file"""


def fsl_histogram_params(
    input_file: InputPathType,
    input_file_duplicate: InputPathType,
    output_file: str,
    output_file_duplicate: str,
    mask_file: InputPathType | None = None,
    mask_file_duplicate: InputPathType | None = None,
    gmmfit_file: InputPathType | None = None,
    gmmfit_file_duplicate: InputPathType | None = None,
    plot_title: str | None = None,
    plot_title_duplicate: str | None = None,
    legend_file: InputPathType | None = None,
    legend_file_duplicate: InputPathType | None = None,
    xlabel: str | None = None,
    xlabel_duplicate: str | None = None,
    ylabel: str | None = None,
    ylabel_duplicate: str | None = None,
    plot_height: float | None = None,
    plot_height_duplicate: float | None = None,
    plot_width: float | None = None,
    plot_width_duplicate: float | None = None,
    num_bins: float | None = None,
    num_bins_duplicate: float | None = None,
    zoom_factor: float | None = None,
    zoom_factor_duplicate: float | None = None,
    use_gmm_flag: bool = False,
) -> FslHistogramParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input file name.
        input_file_duplicate: Input file name.
        output_file: Output filename for the PNG file.
        output_file_duplicate: Output filename for the PNG file.
        mask_file: Mask file name.
        mask_file_duplicate: Mask file name.
        gmmfit_file: File name of matrix with parameter estimates of\
            Gaussian/Gamma mixture model (means, variances and proportions per row).
        gmmfit_file_duplicate: File name of matrix with parameter estimates of\
            Gaussian/Gamma mixture model (means, variances and proportions per row).
        plot_title: Plot title.
        plot_title_duplicate: Plot title.
        legend_file: File name of ASCII text file, one row per legend entry.
        legend_file_duplicate: File name of ASCII text file, one row per legend\
            entry.
        xlabel: X-axis label.
        xlabel_duplicate: X-axis label.
        ylabel: Y-axis label.
        ylabel_duplicate: Y-axis label.
        plot_height: Plot height in pixels (default 400).
        plot_height_duplicate: Plot height in pixels (default 400).
        plot_width: Plot width in pixels (default 600).
        plot_width_duplicate: Plot width in pixels (default 600).
        num_bins: Number of histogram bins.
        num_bins_duplicate: Number of histogram bins.
        zoom_factor: Zoom factor for y-range (e.g. 2.0).
        zoom_factor_duplicate: Zoom factor for y-range (e.g. 2.0).
        use_gmm_flag: Use Gaussian mixture model instead of Gaussian/Gamma\
            mixture model.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_histogram",
        "input_file": input_file,
        "input_file_duplicate": input_file_duplicate,
        "output_file": output_file,
        "output_file_duplicate": output_file_duplicate,
        "use_gmm_flag": use_gmm_flag,
    }
    if mask_file is not None:
        params["mask_file"] = mask_file
    if mask_file_duplicate is not None:
        params["mask_file_duplicate"] = mask_file_duplicate
    if gmmfit_file is not None:
        params["gmmfit_file"] = gmmfit_file
    if gmmfit_file_duplicate is not None:
        params["gmmfit_file_duplicate"] = gmmfit_file_duplicate
    if plot_title is not None:
        params["plot_title"] = plot_title
    if plot_title_duplicate is not None:
        params["plot_title_duplicate"] = plot_title_duplicate
    if legend_file is not None:
        params["legend_file"] = legend_file
    if legend_file_duplicate is not None:
        params["legend_file_duplicate"] = legend_file_duplicate
    if xlabel is not None:
        params["xlabel"] = xlabel
    if xlabel_duplicate is not None:
        params["xlabel_duplicate"] = xlabel_duplicate
    if ylabel is not None:
        params["ylabel"] = ylabel
    if ylabel_duplicate is not None:
        params["ylabel_duplicate"] = ylabel_duplicate
    if plot_height is not None:
        params["plot_height"] = plot_height
    if plot_height_duplicate is not None:
        params["plot_height_duplicate"] = plot_height_duplicate
    if plot_width is not None:
        params["plot_width"] = plot_width
    if plot_width_duplicate is not None:
        params["plot_width_duplicate"] = plot_width_duplicate
    if num_bins is not None:
        params["num_bins"] = num_bins
    if num_bins_duplicate is not None:
        params["num_bins_duplicate"] = num_bins_duplicate
    if zoom_factor is not None:
        params["zoom_factor"] = zoom_factor
    if zoom_factor_duplicate is not None:
        params["zoom_factor_duplicate"] = zoom_factor_duplicate
    return params


def fsl_histogram_cargs(
    params: FslHistogramParameters,
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
    cargs.append("fsl_histogram")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "--in",
        execution.input_file(params.get("input_file_duplicate"))
    ])
    cargs.extend([
        "-o",
        params.get("output_file")
    ])
    cargs.extend([
        "--out",
        params.get("output_file_duplicate")
    ])
    if params.get("mask_file") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("mask_file"))
        ])
    if params.get("mask_file_duplicate") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask_file_duplicate"))
        ])
    if params.get("gmmfit_file") is not None:
        cargs.extend([
            "-f",
            execution.input_file(params.get("gmmfit_file"))
        ])
    if params.get("gmmfit_file_duplicate") is not None:
        cargs.extend([
            "--gmmfit",
            execution.input_file(params.get("gmmfit_file_duplicate"))
        ])
    if params.get("plot_title") is not None:
        cargs.extend([
            "-t",
            params.get("plot_title")
        ])
    if params.get("plot_title_duplicate") is not None:
        cargs.extend([
            "--title",
            params.get("plot_title_duplicate")
        ])
    if params.get("legend_file") is not None:
        cargs.extend([
            "-l",
            execution.input_file(params.get("legend_file"))
        ])
    if params.get("legend_file_duplicate") is not None:
        cargs.extend([
            "--legend",
            execution.input_file(params.get("legend_file_duplicate"))
        ])
    if params.get("xlabel") is not None:
        cargs.extend([
            "-x",
            params.get("xlabel")
        ])
    if params.get("xlabel_duplicate") is not None:
        cargs.extend([
            "--xlabel",
            params.get("xlabel_duplicate")
        ])
    if params.get("ylabel") is not None:
        cargs.extend([
            "-y",
            params.get("ylabel")
        ])
    if params.get("ylabel_duplicate") is not None:
        cargs.extend([
            "--ylabel",
            params.get("ylabel_duplicate")
        ])
    if params.get("plot_height") is not None:
        cargs.extend([
            "-h",
            str(params.get("plot_height"))
        ])
    if params.get("plot_height_duplicate") is not None:
        cargs.extend([
            "--height",
            str(params.get("plot_height_duplicate"))
        ])
    if params.get("plot_width") is not None:
        cargs.extend([
            "-w",
            str(params.get("plot_width"))
        ])
    if params.get("plot_width_duplicate") is not None:
        cargs.extend([
            "--width",
            str(params.get("plot_width_duplicate"))
        ])
    if params.get("num_bins") is not None:
        cargs.extend([
            "-b",
            str(params.get("num_bins"))
        ])
    if params.get("num_bins_duplicate") is not None:
        cargs.extend([
            "--bins",
            str(params.get("num_bins_duplicate"))
        ])
    if params.get("zoom_factor") is not None:
        cargs.extend([
            "-d",
            str(params.get("zoom_factor"))
        ])
    if params.get("zoom_factor_duplicate") is not None:
        cargs.extend([
            "--detail",
            str(params.get("zoom_factor_duplicate"))
        ])
    if params.get("use_gmm_flag"):
        cargs.append("--gmm")
    return cargs


def fsl_histogram_outputs(
    params: FslHistogramParameters,
    execution: Execution,
) -> FslHistogramOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslHistogramOutputs(
        root=execution.output_file("."),
        png_file=execution.output_file(params.get("output_file_duplicate")),
    )
    return ret


def fsl_histogram_execute(
    params: FslHistogramParameters,
    execution: Execution,
) -> FslHistogramOutputs:
    """
    Histogram plotting tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslHistogramOutputs`).
    """
    params = execution.params(params)
    cargs = fsl_histogram_cargs(params, execution)
    ret = fsl_histogram_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_histogram(
    input_file: InputPathType,
    input_file_duplicate: InputPathType,
    output_file: str,
    output_file_duplicate: str,
    mask_file: InputPathType | None = None,
    mask_file_duplicate: InputPathType | None = None,
    gmmfit_file: InputPathType | None = None,
    gmmfit_file_duplicate: InputPathType | None = None,
    plot_title: str | None = None,
    plot_title_duplicate: str | None = None,
    legend_file: InputPathType | None = None,
    legend_file_duplicate: InputPathType | None = None,
    xlabel: str | None = None,
    xlabel_duplicate: str | None = None,
    ylabel: str | None = None,
    ylabel_duplicate: str | None = None,
    plot_height: float | None = None,
    plot_height_duplicate: float | None = None,
    plot_width: float | None = None,
    plot_width_duplicate: float | None = None,
    num_bins: float | None = None,
    num_bins_duplicate: float | None = None,
    zoom_factor: float | None = None,
    zoom_factor_duplicate: float | None = None,
    use_gmm_flag: bool = False,
    runner: Runner | None = None,
) -> FslHistogramOutputs:
    """
    Histogram plotting tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input file name.
        input_file_duplicate: Input file name.
        output_file: Output filename for the PNG file.
        output_file_duplicate: Output filename for the PNG file.
        mask_file: Mask file name.
        mask_file_duplicate: Mask file name.
        gmmfit_file: File name of matrix with parameter estimates of\
            Gaussian/Gamma mixture model (means, variances and proportions per row).
        gmmfit_file_duplicate: File name of matrix with parameter estimates of\
            Gaussian/Gamma mixture model (means, variances and proportions per row).
        plot_title: Plot title.
        plot_title_duplicate: Plot title.
        legend_file: File name of ASCII text file, one row per legend entry.
        legend_file_duplicate: File name of ASCII text file, one row per legend\
            entry.
        xlabel: X-axis label.
        xlabel_duplicate: X-axis label.
        ylabel: Y-axis label.
        ylabel_duplicate: Y-axis label.
        plot_height: Plot height in pixels (default 400).
        plot_height_duplicate: Plot height in pixels (default 400).
        plot_width: Plot width in pixels (default 600).
        plot_width_duplicate: Plot width in pixels (default 600).
        num_bins: Number of histogram bins.
        num_bins_duplicate: Number of histogram bins.
        zoom_factor: Zoom factor for y-range (e.g. 2.0).
        zoom_factor_duplicate: Zoom factor for y-range (e.g. 2.0).
        use_gmm_flag: Use Gaussian mixture model instead of Gaussian/Gamma\
            mixture model.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslHistogramOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_HISTOGRAM_METADATA)
    params = fsl_histogram_params(
        input_file=input_file,
        input_file_duplicate=input_file_duplicate,
        output_file=output_file,
        output_file_duplicate=output_file_duplicate,
        mask_file=mask_file,
        mask_file_duplicate=mask_file_duplicate,
        gmmfit_file=gmmfit_file,
        gmmfit_file_duplicate=gmmfit_file_duplicate,
        plot_title=plot_title,
        plot_title_duplicate=plot_title_duplicate,
        legend_file=legend_file,
        legend_file_duplicate=legend_file_duplicate,
        xlabel=xlabel,
        xlabel_duplicate=xlabel_duplicate,
        ylabel=ylabel,
        ylabel_duplicate=ylabel_duplicate,
        plot_height=plot_height,
        plot_height_duplicate=plot_height_duplicate,
        plot_width=plot_width,
        plot_width_duplicate=plot_width_duplicate,
        num_bins=num_bins,
        num_bins_duplicate=num_bins_duplicate,
        zoom_factor=zoom_factor,
        zoom_factor_duplicate=zoom_factor_duplicate,
        use_gmm_flag=use_gmm_flag,
    )
    return fsl_histogram_execute(params, execution)


__all__ = [
    "FSL_HISTOGRAM_METADATA",
    "FslHistogramOutputs",
    "FslHistogramParameters",
    "fsl_histogram",
    "fsl_histogram_params",
]
