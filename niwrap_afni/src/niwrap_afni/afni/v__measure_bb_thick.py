# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__MEASURE_BB_THICK_METADATA = Metadata(
    id="1c250530ee036924f16cb74f8eac684773e85841.boutiques",
    name="@measure_bb_thick",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VMeasureBbThickParameters = typing.TypedDict('VMeasureBbThickParameters', {
    "__STYX_TYPE__": typing.Literal["@measure_bb_thick"],
    "maskset": InputPathType,
    "surfset": InputPathType,
    "outdir": typing.NotRequired[str | None],
    "resample": typing.NotRequired[str | None],
    "increment": typing.NotRequired[float | None],
    "surfsmooth": typing.NotRequired[float | None],
    "smoothmm": typing.NotRequired[float | None],
    "maxthick": typing.NotRequired[float | None],
    "depth_search": typing.NotRequired[float | None],
    "keep_temp_files": bool,
    "balls_only": bool,
    "surfsmooth_method": typing.NotRequired[str | None],
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
        "@measure_bb_thick": v__measure_bb_thick_cargs,
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
        "@measure_bb_thick": v__measure_bb_thick_outputs,
    }.get(t)


class VMeasureBbThickOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__measure_bb_thick(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    maxfill: OutputPathType | None
    """Thickness/depth dataset"""
    bb_thick: OutputPathType | None
    """Volumetric thickness dataset"""
    bb_thick_smooth: OutputPathType | None
    """Smoothed volumetric thickness dataset"""
    bb_thick_niml: OutputPathType | None
    """Unsmoothed thickness mapped to surface nodes"""
    bb_thick_smooth_niml: OutputPathType | None
    """Smoothed thickness mapped to surface nodes"""
    maskset_output: OutputPathType | None
    """Mask dataset"""
    maskset_resampled: OutputPathType | None
    """Resampled mask dataset"""
    anat_surface: OutputPathType | None
    """Surface representation of mask volume"""
    quick_spec: OutputPathType | None
    """Simple specification file for surface to use with suma commands"""


def v__measure_bb_thick_params(
    maskset: InputPathType,
    surfset: InputPathType,
    outdir: str | None = None,
    resample: str | None = None,
    increment: float | None = None,
    surfsmooth: float | None = None,
    smoothmm: float | None = None,
    maxthick: float | None = None,
    depth_search: float | None = None,
    keep_temp_files: bool = False,
    balls_only: bool = False,
    surfsmooth_method: str | None = None,
) -> VMeasureBbThickParameters:
    """
    Build parameters.
    
    Args:
        maskset: Mask dataset for input.
        surfset: Surface dataset onto which to map thickness (e.g., pial/gray\
            matter surface).
        outdir: Output directory.
        resample: Resample input to mm in millimeters (e.g., half a voxel or\
            'auto'). No resampling is done by default.
        increment: Test thickness at increments of sub-voxel distance. Default\
            is 1/4 voxel minimum distance (in-plane).
        surfsmooth: Smooth surface map of thickness by mm millimeters. Default\
            is 6 mm.
        smoothmm: Smooth volume by mm FWHM in mask. Default is 2*voxelsize of\
            mask or resampled mask.
        maxthick: Search for maximum thickness value of mm millimeters. Default\
            is 6 mm.
        depth_search: Map to surface by looking for max along mm millimeter\
            normal vectors. Default is 3 mm.
        keep_temp_files: Do not delete the intermediate files (for testing).
        balls_only: Calculate only with spheres and skip boxes.
        surfsmooth_method: Heat method used for smoothing surfaces. Default is\
            HEAT_07 but HEAT_05 is also useful for models.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@measure_bb_thick",
        "maskset": maskset,
        "surfset": surfset,
        "keep_temp_files": keep_temp_files,
        "balls_only": balls_only,
    }
    if outdir is not None:
        params["outdir"] = outdir
    if resample is not None:
        params["resample"] = resample
    if increment is not None:
        params["increment"] = increment
    if surfsmooth is not None:
        params["surfsmooth"] = surfsmooth
    if smoothmm is not None:
        params["smoothmm"] = smoothmm
    if maxthick is not None:
        params["maxthick"] = maxthick
    if depth_search is not None:
        params["depth_search"] = depth_search
    if surfsmooth_method is not None:
        params["surfsmooth_method"] = surfsmooth_method
    return params


def v__measure_bb_thick_cargs(
    params: VMeasureBbThickParameters,
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
    cargs.append("@measure_bb_thick")
    cargs.extend([
        "-maskset",
        execution.input_file(params.get("maskset"))
    ])
    cargs.extend([
        "-surfset",
        execution.input_file(params.get("surfset"))
    ])
    if params.get("outdir") is not None:
        cargs.extend([
            "-outdir",
            params.get("outdir")
        ])
    if params.get("resample") is not None:
        cargs.extend([
            "-resample",
            params.get("resample")
        ])
    if params.get("increment") is not None:
        cargs.extend([
            "-increment",
            str(params.get("increment"))
        ])
    if params.get("surfsmooth") is not None:
        cargs.extend([
            "-surfsmooth",
            str(params.get("surfsmooth"))
        ])
    if params.get("smoothmm") is not None:
        cargs.extend([
            "-smoothmm",
            str(params.get("smoothmm"))
        ])
    if params.get("maxthick") is not None:
        cargs.extend([
            "-maxthick",
            str(params.get("maxthick"))
        ])
    if params.get("depth_search") is not None:
        cargs.extend([
            "-depthsearch",
            str(params.get("depth_search"))
        ])
    if params.get("keep_temp_files"):
        cargs.append("-keep_temp_files")
    if params.get("balls_only"):
        cargs.append("-balls_only")
    if params.get("surfsmooth_method") is not None:
        cargs.extend([
            "-surfsmooth_method",
            params.get("surfsmooth_method")
        ])
    return cargs


def v__measure_bb_thick_outputs(
    params: VMeasureBbThickParameters,
    execution: Execution,
) -> VMeasureBbThickOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VMeasureBbThickOutputs(
        root=execution.output_file("."),
        maxfill=execution.output_file(params.get("outdir") + "/maxfill.nii.gz") if (params.get("outdir") is not None) else None,
        bb_thick=execution.output_file(params.get("outdir") + "/bb_thick.nii.gz") if (params.get("outdir") is not None) else None,
        bb_thick_smooth=execution.output_file(params.get("outdir") + "/bb_thick_smooth.nii.gz") if (params.get("outdir") is not None) else None,
        bb_thick_niml=execution.output_file(params.get("outdir") + "/bb_thick.niml.dset") if (params.get("outdir") is not None) else None,
        bb_thick_smooth_niml=execution.output_file(params.get("outdir") + "/bb_thick_smooth.niml.dset") if (params.get("outdir") is not None) else None,
        maskset_output=execution.output_file(params.get("outdir") + "/maskset.nii.gz") if (params.get("outdir") is not None) else None,
        maskset_resampled=execution.output_file(params.get("outdir") + "/maskset_rs.nii.gz") if (params.get("outdir") is not None) else None,
        anat_surface=execution.output_file(params.get("outdir") + "/anat.gii") if (params.get("outdir") is not None) else None,
        quick_spec=execution.output_file(params.get("outdir") + "/quick.spec") if (params.get("outdir") is not None) else None,
    )
    return ret


def v__measure_bb_thick_execute(
    params: VMeasureBbThickParameters,
    execution: Execution,
) -> VMeasureBbThickOutputs:
    """
    Compute thickness of mask using ball and box method.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VMeasureBbThickOutputs`).
    """
    params = execution.params(params)
    cargs = v__measure_bb_thick_cargs(params, execution)
    ret = v__measure_bb_thick_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__measure_bb_thick(
    maskset: InputPathType,
    surfset: InputPathType,
    outdir: str | None = None,
    resample: str | None = None,
    increment: float | None = None,
    surfsmooth: float | None = None,
    smoothmm: float | None = None,
    maxthick: float | None = None,
    depth_search: float | None = None,
    keep_temp_files: bool = False,
    balls_only: bool = False,
    surfsmooth_method: str | None = None,
    runner: Runner | None = None,
) -> VMeasureBbThickOutputs:
    """
    Compute thickness of mask using ball and box method.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        maskset: Mask dataset for input.
        surfset: Surface dataset onto which to map thickness (e.g., pial/gray\
            matter surface).
        outdir: Output directory.
        resample: Resample input to mm in millimeters (e.g., half a voxel or\
            'auto'). No resampling is done by default.
        increment: Test thickness at increments of sub-voxel distance. Default\
            is 1/4 voxel minimum distance (in-plane).
        surfsmooth: Smooth surface map of thickness by mm millimeters. Default\
            is 6 mm.
        smoothmm: Smooth volume by mm FWHM in mask. Default is 2*voxelsize of\
            mask or resampled mask.
        maxthick: Search for maximum thickness value of mm millimeters. Default\
            is 6 mm.
        depth_search: Map to surface by looking for max along mm millimeter\
            normal vectors. Default is 3 mm.
        keep_temp_files: Do not delete the intermediate files (for testing).
        balls_only: Calculate only with spheres and skip boxes.
        surfsmooth_method: Heat method used for smoothing surfaces. Default is\
            HEAT_07 but HEAT_05 is also useful for models.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VMeasureBbThickOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__MEASURE_BB_THICK_METADATA)
    params = v__measure_bb_thick_params(
        maskset=maskset,
        surfset=surfset,
        outdir=outdir,
        resample=resample,
        increment=increment,
        surfsmooth=surfsmooth,
        smoothmm=smoothmm,
        maxthick=maxthick,
        depth_search=depth_search,
        keep_temp_files=keep_temp_files,
        balls_only=balls_only,
        surfsmooth_method=surfsmooth_method,
    )
    return v__measure_bb_thick_execute(params, execution)


__all__ = [
    "VMeasureBbThickOutputs",
    "VMeasureBbThickParameters",
    "V__MEASURE_BB_THICK_METADATA",
    "v__measure_bb_thick",
    "v__measure_bb_thick_params",
]
