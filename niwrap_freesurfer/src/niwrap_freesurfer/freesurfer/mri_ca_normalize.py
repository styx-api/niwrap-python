# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_CA_NORMALIZE_METADATA = Metadata(
    id="d80b2e45336c82ea95d7739d5676f353fb6eb0fb.boutiques",
    name="mri_ca_normalize",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriCaNormalizeParameters = typing.TypedDict('MriCaNormalizeParameters', {
    "__STYXTYPE__": typing.Literal["mri_ca_normalize"],
    "input_brain_volumes": list[InputPathType],
    "atlas_file": InputPathType,
    "xform_file": InputPathType,
    "output_volumes": list[str],
    "seg_file": typing.NotRequired[InputPathType | None],
    "sigma_value": typing.NotRequired[float | None],
    "fsamples_file": typing.NotRequired[InputPathType | None],
    "dilate_iters": typing.NotRequired[float | None],
    "nsamples_file": typing.NotRequired[InputPathType | None],
    "mask_vol": typing.NotRequired[InputPathType | None],
    "control_points_file": typing.NotRequired[InputPathType | None],
    "fonly_file": typing.NotRequired[InputPathType | None],
    "diag_file": typing.NotRequired[InputPathType | None],
    "debug_voxel_coords": typing.NotRequired[list[float] | None],
    "debug_node_coords": typing.NotRequired[list[float] | None],
    "tr_value": typing.NotRequired[float | None],
    "te_value": typing.NotRequired[float | None],
    "alpha_value": typing.NotRequired[float | None],
    "example_mri_vol": typing.NotRequired[InputPathType | None],
    "extra_norm_pctl": typing.NotRequired[float | None],
    "prior_threshold": typing.NotRequired[float | None],
    "n_regions": typing.NotRequired[float | None],
    "verbose_value": typing.NotRequired[float | None],
    "top_percent": typing.NotRequired[float | None],
    "novar_flag": bool,
    "renorm_file": typing.NotRequired[InputPathType | None],
    "flash_flag": bool,
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
        "mri_ca_normalize": mri_ca_normalize_cargs,
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
        "mri_ca_normalize": mri_ca_normalize_outputs,
    }.get(t)


class MriCaNormalizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_ca_normalize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    normalized_output: OutputPathType
    """Normalized output volume in mgh format."""


def mri_ca_normalize_params(
    input_brain_volumes: list[InputPathType],
    atlas_file: InputPathType,
    xform_file: InputPathType,
    output_volumes: list[str],
    seg_file: InputPathType | None = None,
    sigma_value: float | None = None,
    fsamples_file: InputPathType | None = None,
    dilate_iters: float | None = None,
    nsamples_file: InputPathType | None = None,
    mask_vol: InputPathType | None = None,
    control_points_file: InputPathType | None = None,
    fonly_file: InputPathType | None = None,
    diag_file: InputPathType | None = None,
    debug_voxel_coords: list[float] | None = None,
    debug_node_coords: list[float] | None = None,
    tr_value: float | None = None,
    te_value: float | None = None,
    alpha_value: float | None = None,
    example_mri_vol: InputPathType | None = None,
    extra_norm_pctl: float | None = None,
    prior_threshold: float | None = None,
    n_regions: float | None = None,
    verbose_value: float | None = None,
    top_percent: float | None = None,
    novar_flag: bool = False,
    renorm_file: InputPathType | None = None,
    flash_flag: bool = False,
) -> MriCaNormalizeParameters:
    """
    Build parameters.
    
    Args:
        input_brain_volumes: Input brain volume(s). Can specify multiple\
            inputs.
        atlas_file: Atlas file in GCA format.
        xform_file: Transform file in LTA format.
        output_volumes: Output volume(s) in either mgh or mgz format. Can\
            specify multiple outputs.
        seg_file: Aseg file to help normalization.
        sigma_value: Smoothing sigma for bias field if control points specified\
            (default=4).
        fsamples_file: Write control points to filename.
        dilate_iters: Dilate the brain mask niters times before masking.
        nsamples_file: Write transformed normalization control points to\
            filename.
        mask_vol: Use mri_vol to mask input.
        control_points_file: Define control points from filename.
        fonly_file: Only use control points from filename.
        diag_file: Write to log file.
        debug_voxel_coords: Debug voxel. Needs x, y, z coordinates.
        debug_node_coords: Debug node. Needs x, y, z coordinates.
        tr_value: Set TR in msec.
        te_value: Set TE in msec.
        alpha_value: Set alpha in radians.
        example_mri_vol: Use T1 (mri_vol) and segmentation as example.
        extra_norm_pctl: Use 1+pct and 1-pct to widen the range of T1 values.
        prior_threshold: Use prior threshold t (default=.6).
        n_regions: Use n regions/struct for normalization.
        verbose_value: Used for debugging and diagnostics.
        top_percent: Use top p percent (default=.25) white matter points as\
            control points.
        novar_flag: Do not use variance estimates.
        renorm_file: Renormalize using predicted intensity values in mri_vol.
        flash_flag: Use FLASH forward model to predict intensity values.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_ca_normalize",
        "input_brain_volumes": input_brain_volumes,
        "atlas_file": atlas_file,
        "xform_file": xform_file,
        "output_volumes": output_volumes,
        "novar_flag": novar_flag,
        "flash_flag": flash_flag,
    }
    if seg_file is not None:
        params["seg_file"] = seg_file
    if sigma_value is not None:
        params["sigma_value"] = sigma_value
    if fsamples_file is not None:
        params["fsamples_file"] = fsamples_file
    if dilate_iters is not None:
        params["dilate_iters"] = dilate_iters
    if nsamples_file is not None:
        params["nsamples_file"] = nsamples_file
    if mask_vol is not None:
        params["mask_vol"] = mask_vol
    if control_points_file is not None:
        params["control_points_file"] = control_points_file
    if fonly_file is not None:
        params["fonly_file"] = fonly_file
    if diag_file is not None:
        params["diag_file"] = diag_file
    if debug_voxel_coords is not None:
        params["debug_voxel_coords"] = debug_voxel_coords
    if debug_node_coords is not None:
        params["debug_node_coords"] = debug_node_coords
    if tr_value is not None:
        params["tr_value"] = tr_value
    if te_value is not None:
        params["te_value"] = te_value
    if alpha_value is not None:
        params["alpha_value"] = alpha_value
    if example_mri_vol is not None:
        params["example_mri_vol"] = example_mri_vol
    if extra_norm_pctl is not None:
        params["extra_norm_pctl"] = extra_norm_pctl
    if prior_threshold is not None:
        params["prior_threshold"] = prior_threshold
    if n_regions is not None:
        params["n_regions"] = n_regions
    if verbose_value is not None:
        params["verbose_value"] = verbose_value
    if top_percent is not None:
        params["top_percent"] = top_percent
    if renorm_file is not None:
        params["renorm_file"] = renorm_file
    return params


def mri_ca_normalize_cargs(
    params: MriCaNormalizeParameters,
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
    cargs.append("mri_ca_normalize")
    cargs.extend([execution.input_file(f) for f in params.get("input_brain_volumes")])
    cargs.append(execution.input_file(params.get("atlas_file")))
    cargs.append(execution.input_file(params.get("xform_file")))
    cargs.extend(params.get("output_volumes"))
    if params.get("seg_file") is not None:
        cargs.extend([
            "-seg",
            execution.input_file(params.get("seg_file"))
        ])
    if params.get("sigma_value") is not None:
        cargs.extend([
            "-sigma",
            str(params.get("sigma_value"))
        ])
    if params.get("fsamples_file") is not None:
        cargs.extend([
            "-fsamples",
            execution.input_file(params.get("fsamples_file"))
        ])
    if params.get("dilate_iters") is not None:
        cargs.extend([
            "-dilate",
            str(params.get("dilate_iters"))
        ])
    if params.get("nsamples_file") is not None:
        cargs.extend([
            "-nsamples",
            execution.input_file(params.get("nsamples_file"))
        ])
    if params.get("mask_vol") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_vol"))
        ])
    if params.get("control_points_file") is not None:
        cargs.extend([
            "-f",
            execution.input_file(params.get("control_points_file"))
        ])
    if params.get("fonly_file") is not None:
        cargs.extend([
            "-fonly",
            execution.input_file(params.get("fonly_file"))
        ])
    if params.get("diag_file") is not None:
        cargs.extend([
            "-diag",
            execution.input_file(params.get("diag_file"))
        ])
    if params.get("debug_voxel_coords") is not None:
        cargs.extend([
            "-debug_voxel",
            *map(str, params.get("debug_voxel_coords"))
        ])
    if params.get("debug_node_coords") is not None:
        cargs.extend([
            "-debug_node",
            *map(str, params.get("debug_node_coords"))
        ])
    if params.get("tr_value") is not None:
        cargs.extend([
            "-tr",
            str(params.get("tr_value"))
        ])
    if params.get("te_value") is not None:
        cargs.extend([
            "-te",
            str(params.get("te_value"))
        ])
    if params.get("alpha_value") is not None:
        cargs.extend([
            "-alpha",
            str(params.get("alpha_value"))
        ])
    if params.get("example_mri_vol") is not None:
        cargs.extend([
            "-example",
            execution.input_file(params.get("example_mri_vol"))
        ])
    if params.get("extra_norm_pctl") is not None:
        cargs.extend([
            "-extra_norm",
            str(params.get("extra_norm_pctl"))
        ])
    if params.get("prior_threshold") is not None:
        cargs.extend([
            "-prior",
            str(params.get("prior_threshold"))
        ])
    if params.get("n_regions") is not None:
        cargs.extend([
            "-n",
            str(params.get("n_regions"))
        ])
    if params.get("verbose_value") is not None:
        cargs.extend([
            "-v",
            str(params.get("verbose_value"))
        ])
    if params.get("top_percent") is not None:
        cargs.extend([
            "-p",
            str(params.get("top_percent"))
        ])
    if params.get("novar_flag"):
        cargs.append("-novar")
    if params.get("renorm_file") is not None:
        cargs.extend([
            "-renorm",
            execution.input_file(params.get("renorm_file"))
        ])
    if params.get("flash_flag"):
        cargs.append("-flash")
    return cargs


def mri_ca_normalize_outputs(
    params: MriCaNormalizeParameters,
    execution: Execution,
) -> MriCaNormalizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriCaNormalizeOutputs(
        root=execution.output_file("."),
        normalized_output=execution.output_file("output.mgh"),
    )
    return ret


def mri_ca_normalize_execute(
    params: MriCaNormalizeParameters,
    execution: Execution,
) -> MriCaNormalizeOutputs:
    """
    This program creates a normalized volume using the brain volume and an input gca
    file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriCaNormalizeOutputs`).
    """
    params = execution.params(params)
    cargs = mri_ca_normalize_cargs(params, execution)
    ret = mri_ca_normalize_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_ca_normalize(
    input_brain_volumes: list[InputPathType],
    atlas_file: InputPathType,
    xform_file: InputPathType,
    output_volumes: list[str],
    seg_file: InputPathType | None = None,
    sigma_value: float | None = None,
    fsamples_file: InputPathType | None = None,
    dilate_iters: float | None = None,
    nsamples_file: InputPathType | None = None,
    mask_vol: InputPathType | None = None,
    control_points_file: InputPathType | None = None,
    fonly_file: InputPathType | None = None,
    diag_file: InputPathType | None = None,
    debug_voxel_coords: list[float] | None = None,
    debug_node_coords: list[float] | None = None,
    tr_value: float | None = None,
    te_value: float | None = None,
    alpha_value: float | None = None,
    example_mri_vol: InputPathType | None = None,
    extra_norm_pctl: float | None = None,
    prior_threshold: float | None = None,
    n_regions: float | None = None,
    verbose_value: float | None = None,
    top_percent: float | None = None,
    novar_flag: bool = False,
    renorm_file: InputPathType | None = None,
    flash_flag: bool = False,
    runner: Runner | None = None,
) -> MriCaNormalizeOutputs:
    """
    This program creates a normalized volume using the brain volume and an input gca
    file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_brain_volumes: Input brain volume(s). Can specify multiple\
            inputs.
        atlas_file: Atlas file in GCA format.
        xform_file: Transform file in LTA format.
        output_volumes: Output volume(s) in either mgh or mgz format. Can\
            specify multiple outputs.
        seg_file: Aseg file to help normalization.
        sigma_value: Smoothing sigma for bias field if control points specified\
            (default=4).
        fsamples_file: Write control points to filename.
        dilate_iters: Dilate the brain mask niters times before masking.
        nsamples_file: Write transformed normalization control points to\
            filename.
        mask_vol: Use mri_vol to mask input.
        control_points_file: Define control points from filename.
        fonly_file: Only use control points from filename.
        diag_file: Write to log file.
        debug_voxel_coords: Debug voxel. Needs x, y, z coordinates.
        debug_node_coords: Debug node. Needs x, y, z coordinates.
        tr_value: Set TR in msec.
        te_value: Set TE in msec.
        alpha_value: Set alpha in radians.
        example_mri_vol: Use T1 (mri_vol) and segmentation as example.
        extra_norm_pctl: Use 1+pct and 1-pct to widen the range of T1 values.
        prior_threshold: Use prior threshold t (default=.6).
        n_regions: Use n regions/struct for normalization.
        verbose_value: Used for debugging and diagnostics.
        top_percent: Use top p percent (default=.25) white matter points as\
            control points.
        novar_flag: Do not use variance estimates.
        renorm_file: Renormalize using predicted intensity values in mri_vol.
        flash_flag: Use FLASH forward model to predict intensity values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriCaNormalizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CA_NORMALIZE_METADATA)
    params = mri_ca_normalize_params(
        input_brain_volumes=input_brain_volumes,
        atlas_file=atlas_file,
        xform_file=xform_file,
        output_volumes=output_volumes,
        seg_file=seg_file,
        sigma_value=sigma_value,
        fsamples_file=fsamples_file,
        dilate_iters=dilate_iters,
        nsamples_file=nsamples_file,
        mask_vol=mask_vol,
        control_points_file=control_points_file,
        fonly_file=fonly_file,
        diag_file=diag_file,
        debug_voxel_coords=debug_voxel_coords,
        debug_node_coords=debug_node_coords,
        tr_value=tr_value,
        te_value=te_value,
        alpha_value=alpha_value,
        example_mri_vol=example_mri_vol,
        extra_norm_pctl=extra_norm_pctl,
        prior_threshold=prior_threshold,
        n_regions=n_regions,
        verbose_value=verbose_value,
        top_percent=top_percent,
        novar_flag=novar_flag,
        renorm_file=renorm_file,
        flash_flag=flash_flag,
    )
    return mri_ca_normalize_execute(params, execution)


__all__ = [
    "MRI_CA_NORMALIZE_METADATA",
    "MriCaNormalizeOutputs",
    "MriCaNormalizeParameters",
    "mri_ca_normalize",
    "mri_ca_normalize_params",
]
