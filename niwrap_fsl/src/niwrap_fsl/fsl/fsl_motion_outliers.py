# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_MOTION_OUTLIERS_METADATA = Metadata(
    id="32f31b78b1b5679571cc1ab371a618c524911696.boutiques",
    name="fsl_motion_outliers",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslMotionOutliersParameters = typing.TypedDict('FslMotionOutliersParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_motion_outliers"],
    "input_4d_image": InputPathType,
    "output_confound_file": str,
    "mask_image": typing.NotRequired[InputPathType | None],
    "save_metric_file": typing.NotRequired[str | None],
    "save_metric_plot": typing.NotRequired[str | None],
    "temp_path": typing.NotRequired[str | None],
    "refrms_flag": bool,
    "dvars_flag": bool,
    "refmse_flag": bool,
    "fd_flag": bool,
    "fdrms_flag": bool,
    "abs_thresh": typing.NotRequired[float | None],
    "no_moco_flag": bool,
    "dummy_scans": typing.NotRequired[float | None],
    "verbose_flag": bool,
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
        "fsl_motion_outliers": fsl_motion_outliers_cargs,
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
        "fsl_motion_outliers": fsl_motion_outliers_outputs,
    }.get(t)


class FslMotionOutliersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_motion_outliers(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_confound_file: OutputPathType
    """Main output confound file"""
    metric_text_file: OutputPathType | None
    """Metric values saved as text file"""
    metric_plot_file: OutputPathType | None
    """Metric values saved as graphical plot (png format)"""


def fsl_motion_outliers_params(
    input_4d_image: InputPathType,
    output_confound_file: str,
    mask_image: InputPathType | None = None,
    save_metric_file: str | None = None,
    save_metric_plot: str | None = None,
    temp_path: str | None = None,
    refrms_flag: bool = False,
    dvars_flag: bool = False,
    refmse_flag: bool = False,
    fd_flag: bool = False,
    fdrms_flag: bool = False,
    abs_thresh: float | None = None,
    no_moco_flag: bool = False,
    dummy_scans: float | None = None,
    verbose_flag: bool = False,
) -> FslMotionOutliersParameters:
    """
    Build parameters.
    
    Args:
        input_4d_image: Input 4D image (e.g. 4D.nii.gz).
        output_confound_file: Output confound file (e.g. confounds.txt).
        mask_image: Use supplied mask image for calculating metric.
        save_metric_file: Save metric values (e.g. DVARS) as text into\
            specified file.
        save_metric_plot: Save metric values (e.g. DVARS) as a graphical plot\
            (png format).
        temp_path: [Optional] Path to the location where temporary files should\
            be created. Defaults to /tmp.
        refrms_flag: Use RMS intensity difference to reference volume as metric.
        dvars_flag: Use DVARS as metric.
        refmse_flag: Mean Square Error version of --refrms (used in original\
            version of fsl_motion_outliers).
        fd_flag: Use FD (framewise displacement) as metric.
        fdrms_flag: Use FD with RMS matrix calculation as metric.
        abs_thresh: Specify absolute threshold value (otherwise use box-plot\
            cutoff = P75 + 1.5*IQR).
        no_moco_flag: Do not run motion correction (assumed already done).
        dummy_scans: Specify number of dummy scans to delete (before running\
            anything and creating EVs).
        verbose_flag: Verbose mode.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_motion_outliers",
        "input_4d_image": input_4d_image,
        "output_confound_file": output_confound_file,
        "refrms_flag": refrms_flag,
        "dvars_flag": dvars_flag,
        "refmse_flag": refmse_flag,
        "fd_flag": fd_flag,
        "fdrms_flag": fdrms_flag,
        "no_moco_flag": no_moco_flag,
        "verbose_flag": verbose_flag,
    }
    if mask_image is not None:
        params["mask_image"] = mask_image
    if save_metric_file is not None:
        params["save_metric_file"] = save_metric_file
    if save_metric_plot is not None:
        params["save_metric_plot"] = save_metric_plot
    if temp_path is not None:
        params["temp_path"] = temp_path
    if abs_thresh is not None:
        params["abs_thresh"] = abs_thresh
    if dummy_scans is not None:
        params["dummy_scans"] = dummy_scans
    return params


def fsl_motion_outliers_cargs(
    params: FslMotionOutliersParameters,
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
    cargs.append("fsl_motion_outliers")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_4d_image"))
    ])
    cargs.extend([
        "-o",
        params.get("output_confound_file")
    ])
    if params.get("mask_image") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("mask_image"))
        ])
    if params.get("save_metric_file") is not None:
        cargs.extend([
            "-s",
            params.get("save_metric_file")
        ])
    if params.get("save_metric_plot") is not None:
        cargs.extend([
            "-p",
            params.get("save_metric_plot")
        ])
    if params.get("temp_path") is not None:
        cargs.extend([
            "-t",
            params.get("temp_path")
        ])
    if params.get("refrms_flag"):
        cargs.append("--refrms")
    if params.get("dvars_flag"):
        cargs.append("--dvars")
    if params.get("refmse_flag"):
        cargs.append("--refmse")
    if params.get("fd_flag"):
        cargs.append("--fd")
    if params.get("fdrms_flag"):
        cargs.append("--fdrms")
    if params.get("abs_thresh") is not None:
        cargs.extend([
            "--thresh",
            str(params.get("abs_thresh"))
        ])
    if params.get("no_moco_flag"):
        cargs.append("--nomoco")
    if params.get("dummy_scans") is not None:
        cargs.extend([
            "--dummy",
            str(params.get("dummy_scans"))
        ])
    if params.get("verbose_flag"):
        cargs.append("-v")
    return cargs


def fsl_motion_outliers_outputs(
    params: FslMotionOutliersParameters,
    execution: Execution,
) -> FslMotionOutliersOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslMotionOutliersOutputs(
        root=execution.output_file("."),
        output_confound_file=execution.output_file(params.get("output_confound_file")),
        metric_text_file=execution.output_file(params.get("save_metric_file")) if (params.get("save_metric_file") is not None) else None,
        metric_plot_file=execution.output_file(params.get("save_metric_plot")) if (params.get("save_metric_plot") is not None) else None,
    )
    return ret


def fsl_motion_outliers_execute(
    params: FslMotionOutliersParameters,
    execution: Execution,
) -> FslMotionOutliersOutputs:
    """
    FSL tool used to calculate motion outliers in 4D image data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslMotionOutliersOutputs`).
    """
    params = execution.params(params)
    cargs = fsl_motion_outliers_cargs(params, execution)
    ret = fsl_motion_outliers_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_motion_outliers(
    input_4d_image: InputPathType,
    output_confound_file: str,
    mask_image: InputPathType | None = None,
    save_metric_file: str | None = None,
    save_metric_plot: str | None = None,
    temp_path: str | None = None,
    refrms_flag: bool = False,
    dvars_flag: bool = False,
    refmse_flag: bool = False,
    fd_flag: bool = False,
    fdrms_flag: bool = False,
    abs_thresh: float | None = None,
    no_moco_flag: bool = False,
    dummy_scans: float | None = None,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> FslMotionOutliersOutputs:
    """
    FSL tool used to calculate motion outliers in 4D image data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_4d_image: Input 4D image (e.g. 4D.nii.gz).
        output_confound_file: Output confound file (e.g. confounds.txt).
        mask_image: Use supplied mask image for calculating metric.
        save_metric_file: Save metric values (e.g. DVARS) as text into\
            specified file.
        save_metric_plot: Save metric values (e.g. DVARS) as a graphical plot\
            (png format).
        temp_path: [Optional] Path to the location where temporary files should\
            be created. Defaults to /tmp.
        refrms_flag: Use RMS intensity difference to reference volume as metric.
        dvars_flag: Use DVARS as metric.
        refmse_flag: Mean Square Error version of --refrms (used in original\
            version of fsl_motion_outliers).
        fd_flag: Use FD (framewise displacement) as metric.
        fdrms_flag: Use FD with RMS matrix calculation as metric.
        abs_thresh: Specify absolute threshold value (otherwise use box-plot\
            cutoff = P75 + 1.5*IQR).
        no_moco_flag: Do not run motion correction (assumed already done).
        dummy_scans: Specify number of dummy scans to delete (before running\
            anything and creating EVs).
        verbose_flag: Verbose mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslMotionOutliersOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_MOTION_OUTLIERS_METADATA)
    params = fsl_motion_outliers_params(
        input_4d_image=input_4d_image,
        output_confound_file=output_confound_file,
        mask_image=mask_image,
        save_metric_file=save_metric_file,
        save_metric_plot=save_metric_plot,
        temp_path=temp_path,
        refrms_flag=refrms_flag,
        dvars_flag=dvars_flag,
        refmse_flag=refmse_flag,
        fd_flag=fd_flag,
        fdrms_flag=fdrms_flag,
        abs_thresh=abs_thresh,
        no_moco_flag=no_moco_flag,
        dummy_scans=dummy_scans,
        verbose_flag=verbose_flag,
    )
    return fsl_motion_outliers_execute(params, execution)


__all__ = [
    "FSL_MOTION_OUTLIERS_METADATA",
    "FslMotionOutliersOutputs",
    "FslMotionOutliersParameters",
    "fsl_motion_outliers",
    "fsl_motion_outliers_params",
]
