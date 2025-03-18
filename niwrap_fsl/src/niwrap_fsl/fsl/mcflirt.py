# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MCFLIRT_METADATA = Metadata(
    id="49a723958ec897d0bb3510252823e8e366b5aedc.boutiques",
    name="mcflirt",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


McflirtParameters = typing.TypedDict('McflirtParameters', {
    "__STYX_TYPE__": typing.Literal["mcflirt"],
    "in_file": InputPathType,
    "bins": typing.NotRequired[int | None],
    "cost": typing.NotRequired[typing.Literal["mutualinfo", "woods", "corratio", "normcorr", "normmi", "leastsquares"] | None],
    "dof": typing.NotRequired[int | None],
    "init": typing.NotRequired[InputPathType | None],
    "interpolation": typing.NotRequired[typing.Literal["spline_final", "nn_final", "sinc_final"] | None],
    "mean_vol": bool,
    "out_file": typing.NotRequired[str | None],
    "ref_file": typing.NotRequired[InputPathType | None],
    "ref_vol": typing.NotRequired[int | None],
    "rotation": typing.NotRequired[int | None],
    "save_mats": bool,
    "save_plots": bool,
    "save_rmsabs": bool,
    "save_rmsrel": bool,
    "scaling": typing.NotRequired[float | None],
    "smooth": typing.NotRequired[float | None],
    "stages": typing.NotRequired[int | None],
    "stats_imgs": bool,
    "use_contour": bool,
    "use_gradient": bool,
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
        "mcflirt": mcflirt_cargs,
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
        "mcflirt": mcflirt_outputs,
    }.get(t)


class McflirtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mcflirt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mat_file: OutputPathType
    """A list of items which are an existing file name. Transformation
    matrices."""
    mean_img: OutputPathType | None
    """Mean timeseries image (if mean_vol=true)."""
    out_file: OutputPathType | None
    """Motion-corrected timeseries."""
    par_file: OutputPathType | None
    """Text-file with motion parameters."""
    rmsabs_files: OutputPathType | None
    """A list of items which are an existing file name. Absolute displacement
    parameters."""
    rmsrel_files: OutputPathType | None
    """A list of items which are an existing file name. Relative displacement
    parameters."""
    std_img: OutputPathType | None
    """Standard deviation image."""
    variance_img: OutputPathType | None
    """Variance image."""


def mcflirt_params(
    in_file: InputPathType,
    bins: int | None = None,
    cost: typing.Literal["mutualinfo", "woods", "corratio", "normcorr", "normmi", "leastsquares"] | None = None,
    dof: int | None = None,
    init: InputPathType | None = None,
    interpolation: typing.Literal["spline_final", "nn_final", "sinc_final"] | None = None,
    mean_vol: bool = False,
    out_file: str | None = None,
    ref_file: InputPathType | None = None,
    ref_vol: int | None = None,
    rotation: int | None = None,
    save_mats: bool = False,
    save_plots: bool = False,
    save_rmsabs: bool = False,
    save_rmsrel: bool = False,
    scaling: float | None = None,
    smooth: float | None = None,
    stages: int | None = None,
    stats_imgs: bool = False,
    use_contour: bool = False,
    use_gradient: bool = False,
) -> McflirtParameters:
    """
    Build parameters.
    
    Args:
        in_file: Timeseries to motion-correct.
        bins: Number of histogram bins.
        cost: 'mutualinfo' or 'woods' or 'corratio' or 'normcorr' or 'normmi'\
            or 'leastsquares'. Cost function to optimize.
        dof: Degrees of freedom for the transformation.
        init: Initial transformation matrix.
        interpolation: 'spline' or 'nn' or 'sinc'. Interpolation method for\
            transformation.
        mean_vol: Register to mean volume.
        out_file: File to write.
        ref_file: Target image for motion correction.
        ref_vol: Volume to align frames to.
        rotation: Scaling factor for rotation tolerances.
        save_mats: Save transformation matrices.
        save_plots: Save transformation parameters.
        save_rmsabs: Save rms displacement parameters.
        save_rmsrel: Save relative rms displacement parameters.
        scaling: Scaling factor to use.
        smooth: Smoothing factor for the cost function.
        stages: Stages (if 4, perform final search with sinc interpolation.
        stats_imgs: Produce variance and std. dev. images.
        use_contour: Run search on contour images.
        use_gradient: Run search on gradient images.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mcflirt",
        "in_file": in_file,
        "mean_vol": mean_vol,
        "save_mats": save_mats,
        "save_plots": save_plots,
        "save_rmsabs": save_rmsabs,
        "save_rmsrel": save_rmsrel,
        "stats_imgs": stats_imgs,
        "use_contour": use_contour,
        "use_gradient": use_gradient,
    }
    if bins is not None:
        params["bins"] = bins
    if cost is not None:
        params["cost"] = cost
    if dof is not None:
        params["dof"] = dof
    if init is not None:
        params["init"] = init
    if interpolation is not None:
        params["interpolation"] = interpolation
    if out_file is not None:
        params["out_file"] = out_file
    if ref_file is not None:
        params["ref_file"] = ref_file
    if ref_vol is not None:
        params["ref_vol"] = ref_vol
    if rotation is not None:
        params["rotation"] = rotation
    if scaling is not None:
        params["scaling"] = scaling
    if smooth is not None:
        params["smooth"] = smooth
    if stages is not None:
        params["stages"] = stages
    return params


def mcflirt_cargs(
    params: McflirtParameters,
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
    cargs.append("mcflirt")
    cargs.extend([
        "-in",
        execution.input_file(params.get("in_file"))
    ])
    if params.get("bins") is not None:
        cargs.extend([
            "-bins",
            str(params.get("bins"))
        ])
    if params.get("cost") is not None:
        cargs.extend([
            "-cost",
            params.get("cost")
        ])
    if params.get("dof") is not None:
        cargs.extend([
            "-dof",
            str(params.get("dof"))
        ])
    if params.get("init") is not None:
        cargs.extend([
            "-init",
            execution.input_file(params.get("init"))
        ])
    if params.get("interpolation") is not None:
        cargs.append("-" + params.get("interpolation"))
    if params.get("mean_vol"):
        cargs.append("-meanvol")
    if params.get("out_file") is not None:
        cargs.extend([
            "-out",
            params.get("out_file")
        ])
    if params.get("ref_file") is not None:
        cargs.extend([
            "-reffile",
            execution.input_file(params.get("ref_file"))
        ])
    if params.get("ref_vol") is not None:
        cargs.extend([
            "-refvol",
            str(params.get("ref_vol"))
        ])
    if params.get("rotation") is not None:
        cargs.extend([
            "-rotation",
            str(params.get("rotation"))
        ])
    if params.get("save_mats"):
        cargs.append("-mats")
    if params.get("save_plots"):
        cargs.append("-plots")
    if params.get("save_rmsabs"):
        cargs.append("-rmsabs")
    if params.get("save_rmsrel"):
        cargs.append("-rmsrel")
    if params.get("scaling") is not None:
        cargs.extend([
            "-scaling",
            str(params.get("scaling"))
        ])
    if params.get("smooth") is not None:
        cargs.extend([
            "-smooth",
            str(params.get("smooth"))
        ])
    if params.get("stages") is not None:
        cargs.extend([
            "-stages",
            str(params.get("stages"))
        ])
    if params.get("stats_imgs"):
        cargs.append("-stats")
    if params.get("use_contour"):
        cargs.append("-edge")
    if params.get("use_gradient"):
        cargs.append("-gdt")
    return cargs


def mcflirt_outputs(
    params: McflirtParameters,
    execution: Execution,
) -> McflirtOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = McflirtOutputs(
        root=execution.output_file("."),
        mat_file=execution.output_file("MAT_*"),
        mean_img=execution.output_file(params.get("out_file") + "_mean_reg.ext") if (params.get("out_file") is not None) else None,
        out_file=execution.output_file(params.get("out_file")) if (params.get("out_file") is not None) else None,
        par_file=execution.output_file(params.get("out_file") + ".par") if (params.get("out_file") is not None) else None,
        rmsabs_files=execution.output_file(params.get("out_file") + "_abs.rms") if (params.get("out_file") is not None) else None,
        rmsrel_files=execution.output_file(params.get("out_file") + "_rel.rms") if (params.get("out_file") is not None) else None,
        std_img=execution.output_file(params.get("out_file") + "_sigma.ext") if (params.get("out_file") is not None) else None,
        variance_img=execution.output_file(params.get("out_file") + "_variance.ext") if (params.get("out_file") is not None) else None,
    )
    return ret


def mcflirt_execute(
    params: McflirtParameters,
    execution: Execution,
) -> McflirtOutputs:
    """
    MCFLIRT is an intra-modal motion correction tool designed for use on fMRI time
    series and based on optimization and registration techniques used in FLIRT, a
    fully automated robust and accurate tool for linear (affine) inter- and
    inter-modal brain image registration.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `McflirtOutputs`).
    """
    params = execution.params(params)
    cargs = mcflirt_cargs(params, execution)
    ret = mcflirt_outputs(params, execution)
    execution.run(cargs)
    return ret


def mcflirt(
    in_file: InputPathType,
    bins: int | None = None,
    cost: typing.Literal["mutualinfo", "woods", "corratio", "normcorr", "normmi", "leastsquares"] | None = None,
    dof: int | None = None,
    init: InputPathType | None = None,
    interpolation: typing.Literal["spline_final", "nn_final", "sinc_final"] | None = None,
    mean_vol: bool = False,
    out_file: str | None = None,
    ref_file: InputPathType | None = None,
    ref_vol: int | None = None,
    rotation: int | None = None,
    save_mats: bool = False,
    save_plots: bool = False,
    save_rmsabs: bool = False,
    save_rmsrel: bool = False,
    scaling: float | None = None,
    smooth: float | None = None,
    stages: int | None = None,
    stats_imgs: bool = False,
    use_contour: bool = False,
    use_gradient: bool = False,
    runner: Runner | None = None,
) -> McflirtOutputs:
    """
    MCFLIRT is an intra-modal motion correction tool designed for use on fMRI time
    series and based on optimization and registration techniques used in FLIRT, a
    fully automated robust and accurate tool for linear (affine) inter- and
    inter-modal brain image registration.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in_file: Timeseries to motion-correct.
        bins: Number of histogram bins.
        cost: 'mutualinfo' or 'woods' or 'corratio' or 'normcorr' or 'normmi'\
            or 'leastsquares'. Cost function to optimize.
        dof: Degrees of freedom for the transformation.
        init: Initial transformation matrix.
        interpolation: 'spline' or 'nn' or 'sinc'. Interpolation method for\
            transformation.
        mean_vol: Register to mean volume.
        out_file: File to write.
        ref_file: Target image for motion correction.
        ref_vol: Volume to align frames to.
        rotation: Scaling factor for rotation tolerances.
        save_mats: Save transformation matrices.
        save_plots: Save transformation parameters.
        save_rmsabs: Save rms displacement parameters.
        save_rmsrel: Save relative rms displacement parameters.
        scaling: Scaling factor to use.
        smooth: Smoothing factor for the cost function.
        stages: Stages (if 4, perform final search with sinc interpolation.
        stats_imgs: Produce variance and std. dev. images.
        use_contour: Run search on contour images.
        use_gradient: Run search on gradient images.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `McflirtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MCFLIRT_METADATA)
    params = mcflirt_params(
        in_file=in_file,
        bins=bins,
        cost=cost,
        dof=dof,
        init=init,
        interpolation=interpolation,
        mean_vol=mean_vol,
        out_file=out_file,
        ref_file=ref_file,
        ref_vol=ref_vol,
        rotation=rotation,
        save_mats=save_mats,
        save_plots=save_plots,
        save_rmsabs=save_rmsabs,
        save_rmsrel=save_rmsrel,
        scaling=scaling,
        smooth=smooth,
        stages=stages,
        stats_imgs=stats_imgs,
        use_contour=use_contour,
        use_gradient=use_gradient,
    )
    return mcflirt_execute(params, execution)


__all__ = [
    "MCFLIRT_METADATA",
    "McflirtOutputs",
    "McflirtParameters",
    "mcflirt",
    "mcflirt_params",
]
