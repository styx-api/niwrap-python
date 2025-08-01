# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_POLYFIT_METADATA = Metadata(
    id="634ca94604006da564db557fefa10ca9d8de9d9c.boutiques",
    name="3dPolyfit",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dPolyfitParameters = typing.TypedDict('V3dPolyfitParameters', {
    "__STYXTYPE__": typing.Literal["3dPolyfit"],
    "input_dataset": InputPathType,
    "poly_order": typing.NotRequired[int | None],
    "blur": typing.NotRequired[float | None],
    "median_radius": typing.NotRequired[float | None],
    "output_prefix": typing.NotRequired[str | None],
    "resid_prefix": typing.NotRequired[str | None],
    "coeff_output": typing.NotRequired[str | None],
    "automask": bool,
    "mask_dataset": typing.NotRequired[InputPathType | None],
    "mean_scale": bool,
    "clip_box": bool,
    "fit_method": typing.NotRequired[int | None],
    "base_dataset": typing.NotRequired[InputPathType | None],
    "verbose": bool,
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
        "3dPolyfit": v_3d_polyfit_cargs,
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
        "3dPolyfit": v_3d_polyfit_outputs,
    }.get(t)


class V3dPolyfitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_polyfit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Fitted output dataset"""
    resid_file: OutputPathType | None
    """Residual dataset"""
    coeff_file: OutputPathType | None
    """Coefficient output file"""


def v_3d_polyfit_params(
    input_dataset: InputPathType,
    poly_order: int | None = None,
    blur: float | None = None,
    median_radius: float | None = None,
    output_prefix: str | None = None,
    resid_prefix: str | None = None,
    coeff_output: str | None = None,
    automask: bool = False,
    mask_dataset: InputPathType | None = None,
    mean_scale: bool = False,
    clip_box: bool = False,
    fit_method: int | None = None,
    base_dataset: InputPathType | None = None,
    verbose: bool = False,
) -> V3dPolyfitParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset (e.g., data.nii.gz).
        poly_order: Maximum polynomial order (0..9); [default=3]; [n=0 is the\
            constant 1]; [n=-1 means only use volumes from '-base'].
        blur: Gaussian blur input dataset (inside mask) with FWHM='f' (mm).
        median_radius: Radius (voxels) of preliminary median filter of input;\
            default is no blurring.
        output_prefix: Use 'pp' for prefix of output dataset (the fit); default\
            prefix is 'Polyfit'; use NULL to skip this output.
        resid_prefix: Use 'rr' for the prefix of the residual dataset; default\
            is not to output residuals.
        coeff_output: Save coefficients of fit into text file cc.1D; default is\
            not to save these coefficients.
        automask: Create a mask (a la 3dAutomask).
        mask_dataset: Create a mask from nonzero voxels in 'mset'; default is\
            not to use a mask.
        mean_scale: Scale the mean value of the fit (inside the mask) to 1;\
            probably this option is not useful for anything.
        clip_box: Clip fit values outside the rectilinear box containing the\
            mask to the edge of that box, to avoid weird artifacts.
        fit_method: Set 'mm' to 2 for least squares fit; set it to 1 for L1 fit\
            [default method=2]; [Note that L1 fitting is slower than L2 fitting].
        base_dataset: In addition to the polynomial fit, also use the volumes\
            in dataset 'bb' as extra basis functions.
        verbose: Print fun and useful progress reports.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dPolyfit",
        "input_dataset": input_dataset,
        "automask": automask,
        "mean_scale": mean_scale,
        "clip_box": clip_box,
        "verbose": verbose,
    }
    if poly_order is not None:
        params["poly_order"] = poly_order
    if blur is not None:
        params["blur"] = blur
    if median_radius is not None:
        params["median_radius"] = median_radius
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if resid_prefix is not None:
        params["resid_prefix"] = resid_prefix
    if coeff_output is not None:
        params["coeff_output"] = coeff_output
    if mask_dataset is not None:
        params["mask_dataset"] = mask_dataset
    if fit_method is not None:
        params["fit_method"] = fit_method
    if base_dataset is not None:
        params["base_dataset"] = base_dataset
    return params


def v_3d_polyfit_cargs(
    params: V3dPolyfitParameters,
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
    cargs.append("3dPolyfit")
    cargs.append(execution.input_file(params.get("input_dataset")))
    if params.get("poly_order") is not None:
        cargs.extend([
            "-nord",
            str(params.get("poly_order"))
        ])
    if params.get("blur") is not None:
        cargs.extend([
            "-blur",
            str(params.get("blur"))
        ])
    if params.get("median_radius") is not None:
        cargs.extend([
            "-mrad",
            str(params.get("median_radius"))
        ])
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("resid_prefix") is not None:
        cargs.extend([
            "-resid",
            params.get("resid_prefix")
        ])
    if params.get("coeff_output") is not None:
        cargs.extend([
            "-1Dcoef",
            params.get("coeff_output")
        ])
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("mask_dataset") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_dataset"))
        ])
    if params.get("mean_scale"):
        cargs.append("-mone")
    if params.get("clip_box"):
        cargs.append("-mclip")
    if params.get("fit_method") is not None:
        cargs.extend([
            "-meth",
            str(params.get("fit_method"))
        ])
    if params.get("base_dataset") is not None:
        cargs.extend([
            "-base",
            execution.input_file(params.get("base_dataset"))
        ])
    if params.get("verbose"):
        cargs.append("-verb")
    return cargs


def v_3d_polyfit_outputs(
    params: V3dPolyfitParameters,
    execution: Execution,
) -> V3dPolyfitOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dPolyfitOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_prefix") + ".nii.gz") if (params.get("output_prefix") is not None) else None,
        resid_file=execution.output_file(params.get("resid_prefix") + ".nii.gz") if (params.get("resid_prefix") is not None) else None,
        coeff_file=execution.output_file(params.get("coeff_output") + ".1D") if (params.get("coeff_output") is not None) else None,
    )
    return ret


def v_3d_polyfit_execute(
    params: V3dPolyfitParameters,
    execution: Execution,
) -> V3dPolyfitOutputs:
    """
    Fits a polynomial in space to the input dataset and outputs that fitted dataset.
    You can also add your own basis datasets to the fitting mix.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dPolyfitOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_polyfit_cargs(params, execution)
    ret = v_3d_polyfit_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_polyfit(
    input_dataset: InputPathType,
    poly_order: int | None = None,
    blur: float | None = None,
    median_radius: float | None = None,
    output_prefix: str | None = None,
    resid_prefix: str | None = None,
    coeff_output: str | None = None,
    automask: bool = False,
    mask_dataset: InputPathType | None = None,
    mean_scale: bool = False,
    clip_box: bool = False,
    fit_method: int | None = None,
    base_dataset: InputPathType | None = None,
    verbose: bool = False,
    runner: Runner | None = None,
) -> V3dPolyfitOutputs:
    """
    Fits a polynomial in space to the input dataset and outputs that fitted dataset.
    You can also add your own basis datasets to the fitting mix.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset (e.g., data.nii.gz).
        poly_order: Maximum polynomial order (0..9); [default=3]; [n=0 is the\
            constant 1]; [n=-1 means only use volumes from '-base'].
        blur: Gaussian blur input dataset (inside mask) with FWHM='f' (mm).
        median_radius: Radius (voxels) of preliminary median filter of input;\
            default is no blurring.
        output_prefix: Use 'pp' for prefix of output dataset (the fit); default\
            prefix is 'Polyfit'; use NULL to skip this output.
        resid_prefix: Use 'rr' for the prefix of the residual dataset; default\
            is not to output residuals.
        coeff_output: Save coefficients of fit into text file cc.1D; default is\
            not to save these coefficients.
        automask: Create a mask (a la 3dAutomask).
        mask_dataset: Create a mask from nonzero voxels in 'mset'; default is\
            not to use a mask.
        mean_scale: Scale the mean value of the fit (inside the mask) to 1;\
            probably this option is not useful for anything.
        clip_box: Clip fit values outside the rectilinear box containing the\
            mask to the edge of that box, to avoid weird artifacts.
        fit_method: Set 'mm' to 2 for least squares fit; set it to 1 for L1 fit\
            [default method=2]; [Note that L1 fitting is slower than L2 fitting].
        base_dataset: In addition to the polynomial fit, also use the volumes\
            in dataset 'bb' as extra basis functions.
        verbose: Print fun and useful progress reports.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dPolyfitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_POLYFIT_METADATA)
    params = v_3d_polyfit_params(
        input_dataset=input_dataset,
        poly_order=poly_order,
        blur=blur,
        median_radius=median_radius,
        output_prefix=output_prefix,
        resid_prefix=resid_prefix,
        coeff_output=coeff_output,
        automask=automask,
        mask_dataset=mask_dataset,
        mean_scale=mean_scale,
        clip_box=clip_box,
        fit_method=fit_method,
        base_dataset=base_dataset,
        verbose=verbose,
    )
    return v_3d_polyfit_execute(params, execution)


__all__ = [
    "V3dPolyfitOutputs",
    "V3dPolyfitParameters",
    "V_3D_POLYFIT_METADATA",
    "v_3d_polyfit",
    "v_3d_polyfit_params",
]
