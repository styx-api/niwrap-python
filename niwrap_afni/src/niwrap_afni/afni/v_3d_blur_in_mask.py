# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_BLUR_IN_MASK_METADATA = Metadata(
    id="2020eccbab2609356d0e3ab2fdd84a54c25cb900.boutiques",
    name="3dBlurInMask",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dBlurInMaskParameters = typing.TypedDict('V3dBlurInMaskParameters', {
    "__STYX_TYPE__": typing.Literal["3dBlurInMask"],
    "input_file": InputPathType,
    "output_prefix": str,
    "fwhm": float,
    "fwhm_dataset": typing.NotRequired[InputPathType | None],
    "mask": typing.NotRequired[InputPathType | None],
    "multi_mask": typing.NotRequired[InputPathType | None],
    "automask": bool,
    "preserve": bool,
    "quiet": bool,
    "float": bool,
    "fwhm_xyz": typing.NotRequired[list[float] | None],
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
        "3dBlurInMask": v_3d_blur_in_mask_cargs,
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
        "3dBlurInMask": v_3d_blur_in_mask_outputs,
    }.get(t)


class V3dBlurInMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_blur_in_mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output dataset"""


def v_3d_blur_in_mask_params(
    input_file: InputPathType,
    output_prefix: str,
    fwhm: float,
    fwhm_dataset: InputPathType | None = None,
    mask: InputPathType | None = None,
    multi_mask: InputPathType | None = None,
    automask: bool = False,
    preserve: bool = False,
    quiet: bool = False,
    float_: bool = False,
    fwhm_xyz: list[float] | None = None,
) -> V3dBlurInMaskParameters:
    """
    Build parameters.
    
    Args:
        input_file: Dataset to be smoothed and output.
        output_prefix: Prefix for output dataset.
        fwhm: Amount of smoothness to add to the dataset (in mm).
        fwhm_dataset: Dataset containing the amount of smoothness for each\
            voxel.
        mask: Mask dataset for blurring; voxels NOT in the mask will be zeroed\
            in the output.
        multi_mask: Multi-mask dataset; each distinct nonzero value is treated\
            as a separate mask.
        automask: Create an automask from the input dataset.
        preserve: Preserve original values in the dataset outside the mask.
        quiet: Don't be verbose with progress reports.
        float_: Save dataset as floats.
        fwhm_xyz: Add different amounts of smoothness in the 3 spatial\
            directions.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dBlurInMask",
        "input_file": input_file,
        "output_prefix": output_prefix,
        "fwhm": fwhm,
        "automask": automask,
        "preserve": preserve,
        "quiet": quiet,
        "float": float_,
    }
    if fwhm_dataset is not None:
        params["fwhm_dataset"] = fwhm_dataset
    if mask is not None:
        params["mask"] = mask
    if multi_mask is not None:
        params["multi_mask"] = multi_mask
    if fwhm_xyz is not None:
        params["fwhm_xyz"] = fwhm_xyz
    return params


def v_3d_blur_in_mask_cargs(
    params: V3dBlurInMaskParameters,
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
    cargs.append("3dBlurInMask")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_prefix"))
    cargs.extend([
        "-FWHM",
        str(params.get("fwhm"))
    ])
    if params.get("fwhm_dataset") is not None:
        cargs.extend([
            "-FWHMdset",
            execution.input_file(params.get("fwhm_dataset"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("multi_mask") is not None:
        cargs.extend([
            "-Mmask",
            execution.input_file(params.get("multi_mask"))
        ])
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("preserve"):
        cargs.append("-preserve")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("float"):
        cargs.append("-float")
    if params.get("fwhm_xyz") is not None:
        cargs.extend([
            "-FWHMxyz",
            *map(str, params.get("fwhm_xyz"))
        ])
    return cargs


def v_3d_blur_in_mask_outputs(
    params: V3dBlurInMaskParameters,
    execution: Execution,
) -> V3dBlurInMaskOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dBlurInMaskOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_prefix")),
    )
    return ret


def v_3d_blur_in_mask_execute(
    params: V3dBlurInMaskParameters,
    execution: Execution,
) -> V3dBlurInMaskOutputs:
    """
    Blurs a dataset spatially inside a mask.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dBlurInMaskOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_blur_in_mask_cargs(params, execution)
    ret = v_3d_blur_in_mask_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_blur_in_mask(
    input_file: InputPathType,
    output_prefix: str,
    fwhm: float,
    fwhm_dataset: InputPathType | None = None,
    mask: InputPathType | None = None,
    multi_mask: InputPathType | None = None,
    automask: bool = False,
    preserve: bool = False,
    quiet: bool = False,
    float_: bool = False,
    fwhm_xyz: list[float] | None = None,
    runner: Runner | None = None,
) -> V3dBlurInMaskOutputs:
    """
    Blurs a dataset spatially inside a mask.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Dataset to be smoothed and output.
        output_prefix: Prefix for output dataset.
        fwhm: Amount of smoothness to add to the dataset (in mm).
        fwhm_dataset: Dataset containing the amount of smoothness for each\
            voxel.
        mask: Mask dataset for blurring; voxels NOT in the mask will be zeroed\
            in the output.
        multi_mask: Multi-mask dataset; each distinct nonzero value is treated\
            as a separate mask.
        automask: Create an automask from the input dataset.
        preserve: Preserve original values in the dataset outside the mask.
        quiet: Don't be verbose with progress reports.
        float_: Save dataset as floats.
        fwhm_xyz: Add different amounts of smoothness in the 3 spatial\
            directions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dBlurInMaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BLUR_IN_MASK_METADATA)
    params = v_3d_blur_in_mask_params(
        input_file=input_file,
        output_prefix=output_prefix,
        fwhm=fwhm,
        fwhm_dataset=fwhm_dataset,
        mask=mask,
        multi_mask=multi_mask,
        automask=automask,
        preserve=preserve,
        quiet=quiet,
        float_=float_,
        fwhm_xyz=fwhm_xyz,
    )
    return v_3d_blur_in_mask_execute(params, execution)


__all__ = [
    "V3dBlurInMaskOutputs",
    "V3dBlurInMaskParameters",
    "V_3D_BLUR_IN_MASK_METADATA",
    "v_3d_blur_in_mask",
    "v_3d_blur_in_mask_params",
]
