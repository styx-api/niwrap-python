# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_2DCAT_METADATA = Metadata(
    id="1ff7d0dc60f4bf318c5c16752466d2ad9856a898.boutiques",
    name="2dcat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V2dcatParameters = typing.TypedDict('V2dcatParameters', {
    "__STYX_TYPE__": typing.Literal["2dcat"],
    "filenames": list[InputPathType],
    "scale_image": typing.NotRequired[InputPathType | None],
    "scale_pixels": typing.NotRequired[InputPathType | None],
    "scale_intensity": bool,
    "gscale": typing.NotRequired[float | None],
    "rgb_out": bool,
    "res_in": typing.NotRequired[list[float] | None],
    "respad_in": typing.NotRequired[list[float] | None],
    "pad_val": typing.NotRequired[float | None],
    "crop": typing.NotRequired[list[float] | None],
    "autocrop_ctol": typing.NotRequired[float | None],
    "autocrop_atol": typing.NotRequired[float | None],
    "autocrop": bool,
    "zero_wrap": bool,
    "white_wrap": bool,
    "gray_wrap": typing.NotRequired[float | None],
    "image_wrap": bool,
    "rand_wrap": bool,
    "prefix": typing.NotRequired[str | None],
    "matrix": typing.NotRequired[list[float] | None],
    "nx": typing.NotRequired[float | None],
    "ny": typing.NotRequired[float | None],
    "matrix_from_scale": bool,
    "gap": typing.NotRequired[float | None],
    "gap_col": typing.NotRequired[list[float] | None],
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
        "2dcat": v_2dcat_cargs,
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
        "2dcat": v_2dcat_outputs,
    }.get(t)


class V2dcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_2dcat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType | None
    """The main output image matrix file."""
    output_1_d: OutputPathType | None
    """A 1D file containing the average of RGB values, if the prefix ends with
    .1D."""


def v_2dcat_params(
    filenames: list[InputPathType],
    scale_image: InputPathType | None = None,
    scale_pixels: InputPathType | None = None,
    scale_intensity: bool = False,
    gscale: float | None = None,
    rgb_out: bool = False,
    res_in: list[float] | None = None,
    respad_in: list[float] | None = None,
    pad_val: float | None = None,
    crop: list[float] | None = None,
    autocrop_ctol: float | None = None,
    autocrop_atol: float | None = None,
    autocrop: bool = False,
    zero_wrap: bool = False,
    white_wrap: bool = False,
    gray_wrap: float | None = None,
    image_wrap: bool = False,
    rand_wrap: bool = False,
    prefix: str | None = None,
    matrix: list[float] | None = None,
    nx: float | None = None,
    ny: float | None = None,
    matrix_from_scale: bool = False,
    gap: float | None = None,
    gap_col: list[float] | None = None,
) -> V2dcatParameters:
    """
    Build parameters.
    
    Args:
        filenames: List of input image files.
        scale_image: Multiply each image in the output image matrix by the\
            color or intensity of the pixel in the scale image.
        scale_pixels: Multiply each pixel in the output image by the color or\
            intensity of the pixel in the scale image. The scale image is resized\
            to the output image's resolution.
        scale_intensity: Use the intensity (average color) of the pixel instead\
            of its color.
        gscale: Apply additional scaling factor.
        rgb_out: Force output to be in RGB, even if input is bytes.
        res_in: Set resolution of all input images.
        respad_in: Resample to max while respecting the aspect ratio, then pad\
            to desired pixel count.
        pad_val: Set the padding value when using -respad_in. Should be in the\
            range [0, 255], default is 0.
        crop: Crop images by specified number of pixels from the left, right,\
            top, and bottom.
        autocrop_ctol: Automatically crop lines where RGB values differ by less\
            than the specified percentage from the corner pixel values.
        autocrop_atol: Automatically crop lines where RGB values differ by less\
            than the specified percentage from the line average.
        autocrop: Automatically crop lines with default tolerances using both\
            autocrop_atol and autocrop_ctol set to 20.
        zero_wrap: Use solid black images if not enough images are provided to\
            fill the matrix.
        white_wrap: Use solid white images if not enough images are provided to\
            fill the matrix.
        gray_wrap: Use solid gray images if not enough images are provided to\
            fill the matrix. The gray value must be between 0 and 1.0.
        image_wrap: Reuse images to fill the matrix. This is the default\
            behavior.
        rand_wrap: Randomize the order of images when reusing to fill the\
            matrix.
        prefix: Prefix the output file names with the specified string.
        matrix: Specify the number of images in each row (NX) and column (NY)\
            of the image matrix.
        nx: Specify the number of images in each row.
        ny: Specify the number of images in each column.
        matrix_from_scale: Set matrix dimensions NX and NY to be the same as\
            the SCALE_IMG's dimensions. Requires the -scale_image option.
        gap: Put a gap of specified pixels between images.
        gap_col: Set color of the gap line to specified R, G, B values. Values\
            range from 0 to 255.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "2dcat",
        "filenames": filenames,
        "scale_intensity": scale_intensity,
        "rgb_out": rgb_out,
        "autocrop": autocrop,
        "zero_wrap": zero_wrap,
        "white_wrap": white_wrap,
        "image_wrap": image_wrap,
        "rand_wrap": rand_wrap,
        "matrix_from_scale": matrix_from_scale,
    }
    if scale_image is not None:
        params["scale_image"] = scale_image
    if scale_pixels is not None:
        params["scale_pixels"] = scale_pixels
    if gscale is not None:
        params["gscale"] = gscale
    if res_in is not None:
        params["res_in"] = res_in
    if respad_in is not None:
        params["respad_in"] = respad_in
    if pad_val is not None:
        params["pad_val"] = pad_val
    if crop is not None:
        params["crop"] = crop
    if autocrop_ctol is not None:
        params["autocrop_ctol"] = autocrop_ctol
    if autocrop_atol is not None:
        params["autocrop_atol"] = autocrop_atol
    if gray_wrap is not None:
        params["gray_wrap"] = gray_wrap
    if prefix is not None:
        params["prefix"] = prefix
    if matrix is not None:
        params["matrix"] = matrix
    if nx is not None:
        params["nx"] = nx
    if ny is not None:
        params["ny"] = ny
    if gap is not None:
        params["gap"] = gap
    if gap_col is not None:
        params["gap_col"] = gap_col
    return params


def v_2dcat_cargs(
    params: V2dcatParameters,
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
    cargs.append("2dcat")
    cargs.extend([execution.input_file(f) for f in params.get("filenames")])
    if params.get("scale_image") is not None:
        cargs.extend([
            "-scale_image",
            execution.input_file(params.get("scale_image"))
        ])
    if params.get("scale_pixels") is not None:
        cargs.extend([
            "-scale_pixels",
            execution.input_file(params.get("scale_pixels"))
        ])
    if params.get("scale_intensity"):
        cargs.append("-scale_intensity")
    if params.get("gscale") is not None:
        cargs.extend([
            "-gscale",
            str(params.get("gscale"))
        ])
    if params.get("rgb_out"):
        cargs.append("-rgb_out")
    if params.get("res_in") is not None:
        cargs.extend([
            "-res_in",
            *map(str, params.get("res_in"))
        ])
    if params.get("respad_in") is not None:
        cargs.extend([
            "-respad_in",
            *map(str, params.get("respad_in"))
        ])
    if params.get("pad_val") is not None:
        cargs.extend([
            "-pad_val",
            str(params.get("pad_val"))
        ])
    if params.get("crop") is not None:
        cargs.extend([
            "-crop",
            *map(str, params.get("crop"))
        ])
    if params.get("autocrop_ctol") is not None:
        cargs.extend([
            "-autocrop_ctol",
            str(params.get("autocrop_ctol"))
        ])
    if params.get("autocrop_atol") is not None:
        cargs.extend([
            "-autocrop_atol",
            str(params.get("autocrop_atol"))
        ])
    if params.get("autocrop"):
        cargs.append("-autocrop")
    if params.get("zero_wrap"):
        cargs.append("-zero_wrap")
    if params.get("white_wrap"):
        cargs.append("-white_wrap")
    if params.get("gray_wrap") is not None:
        cargs.extend([
            "-gray_wrap",
            str(params.get("gray_wrap"))
        ])
    if params.get("image_wrap"):
        cargs.append("-image_wrap")
    if params.get("rand_wrap"):
        cargs.append("-rand_wrap")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("matrix") is not None:
        cargs.extend([
            "-matrix",
            *map(str, params.get("matrix"))
        ])
    if params.get("nx") is not None:
        cargs.extend([
            "-nx",
            str(params.get("nx"))
        ])
    if params.get("ny") is not None:
        cargs.extend([
            "-ny",
            str(params.get("ny"))
        ])
    if params.get("matrix_from_scale"):
        cargs.append("-matrix_from_scale")
    if params.get("gap") is not None:
        cargs.extend([
            "-gap",
            str(params.get("gap"))
        ])
    if params.get("gap_col") is not None:
        cargs.extend([
            "-gap_col",
            *map(str, params.get("gap_col"))
        ])
    return cargs


def v_2dcat_outputs(
    params: V2dcatParameters,
    execution: Execution,
) -> V2dcatOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V2dcatOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(params.get("prefix") + ".ppm") if (params.get("prefix") is not None) else None,
        output_1_d=execution.output_file(params.get("prefix") + ".1D") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_2dcat_execute(
    params: V2dcatParameters,
    execution: Execution,
) -> V2dcatOutputs:
    """
    Puts a set of images into an image matrix montage of NX by NY images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V2dcatOutputs`).
    """
    params = execution.params(params)
    cargs = v_2dcat_cargs(params, execution)
    ret = v_2dcat_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_2dcat(
    filenames: list[InputPathType],
    scale_image: InputPathType | None = None,
    scale_pixels: InputPathType | None = None,
    scale_intensity: bool = False,
    gscale: float | None = None,
    rgb_out: bool = False,
    res_in: list[float] | None = None,
    respad_in: list[float] | None = None,
    pad_val: float | None = None,
    crop: list[float] | None = None,
    autocrop_ctol: float | None = None,
    autocrop_atol: float | None = None,
    autocrop: bool = False,
    zero_wrap: bool = False,
    white_wrap: bool = False,
    gray_wrap: float | None = None,
    image_wrap: bool = False,
    rand_wrap: bool = False,
    prefix: str | None = None,
    matrix: list[float] | None = None,
    nx: float | None = None,
    ny: float | None = None,
    matrix_from_scale: bool = False,
    gap: float | None = None,
    gap_col: list[float] | None = None,
    runner: Runner | None = None,
) -> V2dcatOutputs:
    """
    Puts a set of images into an image matrix montage of NX by NY images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        filenames: List of input image files.
        scale_image: Multiply each image in the output image matrix by the\
            color or intensity of the pixel in the scale image.
        scale_pixels: Multiply each pixel in the output image by the color or\
            intensity of the pixel in the scale image. The scale image is resized\
            to the output image's resolution.
        scale_intensity: Use the intensity (average color) of the pixel instead\
            of its color.
        gscale: Apply additional scaling factor.
        rgb_out: Force output to be in RGB, even if input is bytes.
        res_in: Set resolution of all input images.
        respad_in: Resample to max while respecting the aspect ratio, then pad\
            to desired pixel count.
        pad_val: Set the padding value when using -respad_in. Should be in the\
            range [0, 255], default is 0.
        crop: Crop images by specified number of pixels from the left, right,\
            top, and bottom.
        autocrop_ctol: Automatically crop lines where RGB values differ by less\
            than the specified percentage from the corner pixel values.
        autocrop_atol: Automatically crop lines where RGB values differ by less\
            than the specified percentage from the line average.
        autocrop: Automatically crop lines with default tolerances using both\
            autocrop_atol and autocrop_ctol set to 20.
        zero_wrap: Use solid black images if not enough images are provided to\
            fill the matrix.
        white_wrap: Use solid white images if not enough images are provided to\
            fill the matrix.
        gray_wrap: Use solid gray images if not enough images are provided to\
            fill the matrix. The gray value must be between 0 and 1.0.
        image_wrap: Reuse images to fill the matrix. This is the default\
            behavior.
        rand_wrap: Randomize the order of images when reusing to fill the\
            matrix.
        prefix: Prefix the output file names with the specified string.
        matrix: Specify the number of images in each row (NX) and column (NY)\
            of the image matrix.
        nx: Specify the number of images in each row.
        ny: Specify the number of images in each column.
        matrix_from_scale: Set matrix dimensions NX and NY to be the same as\
            the SCALE_IMG's dimensions. Requires the -scale_image option.
        gap: Put a gap of specified pixels between images.
        gap_col: Set color of the gap line to specified R, G, B values. Values\
            range from 0 to 255.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V2dcatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_2DCAT_METADATA)
    params = v_2dcat_params(
        filenames=filenames,
        scale_image=scale_image,
        scale_pixels=scale_pixels,
        scale_intensity=scale_intensity,
        gscale=gscale,
        rgb_out=rgb_out,
        res_in=res_in,
        respad_in=respad_in,
        pad_val=pad_val,
        crop=crop,
        autocrop_ctol=autocrop_ctol,
        autocrop_atol=autocrop_atol,
        autocrop=autocrop,
        zero_wrap=zero_wrap,
        white_wrap=white_wrap,
        gray_wrap=gray_wrap,
        image_wrap=image_wrap,
        rand_wrap=rand_wrap,
        prefix=prefix,
        matrix=matrix,
        nx=nx,
        ny=ny,
        matrix_from_scale=matrix_from_scale,
        gap=gap,
        gap_col=gap_col,
    )
    return v_2dcat_execute(params, execution)


__all__ = [
    "V2dcatOutputs",
    "V2dcatParameters",
    "V_2DCAT_METADATA",
    "v_2dcat",
    "v_2dcat_params",
]
