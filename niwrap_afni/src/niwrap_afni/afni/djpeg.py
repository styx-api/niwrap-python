# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DJPEG_METADATA = Metadata(
    id="9c5e3f0913e97439eefa4801b85b0734d0587e4a.boutiques",
    name="djpeg",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


DjpegParameters = typing.TypedDict('DjpegParameters', {
    "__STYX_TYPE__": typing.Literal["djpeg"],
    "input_file": InputPathType,
    "output_file": str,
    "gray": bool,
    "fast_dct": bool,
    "one_pixel_height": bool,
    "pseudo_pixel_ratio": bool,
    "crop_region": typing.NotRequired[str | None],
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
        "djpeg": djpeg_cargs,
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
        "djpeg": djpeg_outputs,
    }.get(t)


class DjpegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `djpeg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """Output image file"""


def djpeg_params(
    input_file: InputPathType,
    output_file: str,
    gray: bool = False,
    fast_dct: bool = False,
    one_pixel_height: bool = False,
    pseudo_pixel_ratio: bool = False,
    crop_region: str | None = None,
) -> DjpegParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input JPEG file (e.g. image.jpg).
        output_file: Output image file (e.g. image.ppm).
        gray: Force grayscale output.
        fast_dct: Prevent dithering of output.
        one_pixel_height: Force one-pixel modulation flag.
        pseudo_pixel_ratio: Force pseudo-pixel ratio flag.
        crop_region: Crop region (syntax: WxH+X+Y, e.g., 100x100+10+10).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "djpeg",
        "input_file": input_file,
        "output_file": output_file,
        "gray": gray,
        "fast_dct": fast_dct,
        "one_pixel_height": one_pixel_height,
        "pseudo_pixel_ratio": pseudo_pixel_ratio,
    }
    if crop_region is not None:
        params["crop_region"] = crop_region
    return params


def djpeg_cargs(
    params: DjpegParameters,
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
    cargs.append("djpeg")
    cargs.append(execution.input_file(params.get("input_file")))
    cargs.append(params.get("output_file"))
    if params.get("gray"):
        cargs.append("-grayscale")
    if params.get("fast_dct"):
        cargs.append("-fast")
    if params.get("one_pixel_height"):
        cargs.append("-onepixel")
    if params.get("pseudo_pixel_ratio"):
        cargs.append("-236")
    if params.get("crop_region") is not None:
        cargs.extend([
            "-crop",
            params.get("crop_region")
        ])
    return cargs


def djpeg_outputs(
    params: DjpegParameters,
    execution: Execution,
) -> DjpegOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DjpegOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(params.get("output_file")),
    )
    return ret


def djpeg_execute(
    params: DjpegParameters,
    execution: Execution,
) -> DjpegOutputs:
    """
    Decompress a JPEG file to an image file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DjpegOutputs`).
    """
    params = execution.params(params)
    cargs = djpeg_cargs(params, execution)
    ret = djpeg_outputs(params, execution)
    execution.run(cargs)
    return ret


def djpeg(
    input_file: InputPathType,
    output_file: str,
    gray: bool = False,
    fast_dct: bool = False,
    one_pixel_height: bool = False,
    pseudo_pixel_ratio: bool = False,
    crop_region: str | None = None,
    runner: Runner | None = None,
) -> DjpegOutputs:
    """
    Decompress a JPEG file to an image file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input JPEG file (e.g. image.jpg).
        output_file: Output image file (e.g. image.ppm).
        gray: Force grayscale output.
        fast_dct: Prevent dithering of output.
        one_pixel_height: Force one-pixel modulation flag.
        pseudo_pixel_ratio: Force pseudo-pixel ratio flag.
        crop_region: Crop region (syntax: WxH+X+Y, e.g., 100x100+10+10).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DjpegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DJPEG_METADATA)
    params = djpeg_params(
        input_file=input_file,
        output_file=output_file,
        gray=gray,
        fast_dct=fast_dct,
        one_pixel_height=one_pixel_height,
        pseudo_pixel_ratio=pseudo_pixel_ratio,
        crop_region=crop_region,
    )
    return djpeg_execute(params, execution)


__all__ = [
    "DJPEG_METADATA",
    "DjpegOutputs",
    "DjpegParameters",
    "djpeg",
    "djpeg_params",
]
