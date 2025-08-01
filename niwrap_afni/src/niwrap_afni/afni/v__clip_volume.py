# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__CLIP_VOLUME_METADATA = Metadata(
    id="0999d3039fac00d441e01a61ca33ad8ceb36a238.boutiques",
    name="@clip_volume",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VClipVolumeParameters = typing.TypedDict('VClipVolumeParameters', {
    "__STYXTYPE__": typing.Literal["@clip_volume"],
    "input_volume": InputPathType,
    "below_zmm": typing.NotRequired[float | None],
    "above_zmm": typing.NotRequired[float | None],
    "left_xmm": typing.NotRequired[float | None],
    "right_xmm": typing.NotRequired[float | None],
    "anterior_ymm": typing.NotRequired[float | None],
    "posterior_ymm": typing.NotRequired[float | None],
    "box": typing.NotRequired[list[float] | None],
    "mask_box": typing.NotRequired[list[float] | None],
    "and_logic": bool,
    "or_logic": bool,
    "verbosity": bool,
    "crop_allzero": bool,
    "crop_greedy": bool,
    "crop": bool,
    "crop_npad": typing.NotRequired[float | None],
    "output_prefix": typing.NotRequired[str | None],
    "followers": typing.NotRequired[list[InputPathType] | None],
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
        "@clip_volume": v__clip_volume_cargs,
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
        "@clip_volume": v__clip_volume_outputs,
    }.get(t)


class VClipVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__clip_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_clipped_volume: OutputPathType | None
    """Output clipped or cropped volume"""
    output_followers: OutputPathType | None
    """Output for follower datasets after clipping/cropping"""


def v__clip_volume_params(
    input_volume: InputPathType,
    below_zmm: float | None = None,
    above_zmm: float | None = None,
    left_xmm: float | None = None,
    right_xmm: float | None = None,
    anterior_ymm: float | None = None,
    posterior_ymm: float | None = None,
    box: list[float] | None = None,
    mask_box: list[float] | None = None,
    and_logic: bool = False,
    or_logic: bool = False,
    verbosity: bool = False,
    crop_allzero: bool = False,
    crop_greedy: bool = False,
    crop: bool = False,
    crop_npad: float | None = None,
    output_prefix: str | None = None,
    followers: list[InputPathType] | None = None,
) -> VClipVolumeParameters:
    """
    Build parameters.
    
    Args:
        input_volume: Volume to clip.
        below_zmm: Set to 0 slices below Zmm.
        above_zmm: Set to 0 slices above Zmm.
        left_xmm: Set to 0 slices left of Xmm.
        right_xmm: Set to 0 slices right of Xmm.
        anterior_ymm: Set to 0 slices anterior to Ymm.
        posterior_ymm: Set to 0 slices posterior to Ymm.
        box: Clip the volume to a box centered at Cx, Cy, Cz (RAI mm), and of\
            dimensions Dx Dy Dz (RAI mm).
        mask_box: Set all values inside the box to 1. Box centered at Cx, Cy,\
            Cz (RAI mm), and of dimensions Dx Dy Dz (RAI mm).
        and_logic: Combine with next clipping planes using 'and'.
        or_logic: Combine with next clipping planes using 'or'.
        verbosity: Show command details (verbose output).
        crop_allzero: Crop the output volume with 3dAutobox -noclust.
        crop_greedy: Crop the output volume with 3dAutobox.
        crop: Same as -crop_greedy, kept for backward compatibility.
        crop_npad: Set 3dAutobox's -npad option to NPAD. NPAD fattens the\
            volume a little after cropping.
        output_prefix: Output prefix for the resultant volume. Default is the\
            input prefix with _clp suffixed to it.
        followers: Apply the same clipping or cropping treatment to the\
            follower datasets.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@clip_volume",
        "input_volume": input_volume,
        "and_logic": and_logic,
        "or_logic": or_logic,
        "verbosity": verbosity,
        "crop_allzero": crop_allzero,
        "crop_greedy": crop_greedy,
        "crop": crop,
    }
    if below_zmm is not None:
        params["below_zmm"] = below_zmm
    if above_zmm is not None:
        params["above_zmm"] = above_zmm
    if left_xmm is not None:
        params["left_xmm"] = left_xmm
    if right_xmm is not None:
        params["right_xmm"] = right_xmm
    if anterior_ymm is not None:
        params["anterior_ymm"] = anterior_ymm
    if posterior_ymm is not None:
        params["posterior_ymm"] = posterior_ymm
    if box is not None:
        params["box"] = box
    if mask_box is not None:
        params["mask_box"] = mask_box
    if crop_npad is not None:
        params["crop_npad"] = crop_npad
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if followers is not None:
        params["followers"] = followers
    return params


def v__clip_volume_cargs(
    params: VClipVolumeParameters,
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
    cargs.append("@clip_volume")
    cargs.append(execution.input_file(params.get("input_volume")))
    if params.get("below_zmm") is not None:
        cargs.extend([
            "-below",
            str(params.get("below_zmm"))
        ])
    if params.get("above_zmm") is not None:
        cargs.extend([
            "-above",
            str(params.get("above_zmm"))
        ])
    if params.get("left_xmm") is not None:
        cargs.extend([
            "-left",
            str(params.get("left_xmm"))
        ])
    if params.get("right_xmm") is not None:
        cargs.extend([
            "-right",
            str(params.get("right_xmm"))
        ])
    if params.get("anterior_ymm") is not None:
        cargs.extend([
            "-anterior",
            str(params.get("anterior_ymm"))
        ])
    if params.get("posterior_ymm") is not None:
        cargs.extend([
            "-posterior",
            str(params.get("posterior_ymm"))
        ])
    if params.get("box") is not None:
        cargs.extend([
            "-box",
            *map(str, params.get("box"))
        ])
    if params.get("mask_box") is not None:
        cargs.extend([
            "-mask_box",
            *map(str, params.get("mask_box"))
        ])
    if params.get("and_logic"):
        cargs.append("-and")
    if params.get("or_logic"):
        cargs.append("-or")
    if params.get("verbosity"):
        cargs.append("-verb")
    if params.get("crop_allzero"):
        cargs.append("-crop_allzero")
    if params.get("crop_greedy"):
        cargs.append("-crop_greedy")
    if params.get("crop"):
        cargs.append("-crop")
    if params.get("crop_npad") is not None:
        cargs.extend([
            "-crop_npad",
            str(params.get("crop_npad"))
        ])
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("followers") is not None:
        cargs.extend([
            "-followers",
            *[execution.input_file(f) for f in params.get("followers")]
        ])
    return cargs


def v__clip_volume_outputs(
    params: VClipVolumeParameters,
    execution: Execution,
) -> VClipVolumeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VClipVolumeOutputs(
        root=execution.output_file("."),
        output_clipped_volume=execution.output_file(params.get("output_prefix") + "_clp.nii.gz") if (params.get("output_prefix") is not None) else None,
        output_followers=execution.output_file(params.get("output_prefix") + "_follow_clp.nii.gz") if (params.get("output_prefix") is not None) else None,
    )
    return ret


def v__clip_volume_execute(
    params: VClipVolumeParameters,
    execution: Execution,
) -> VClipVolumeOutputs:
    """
    A tool to clip regions of a volume in various ways, such as above/below certain
    coordinates or within a specified box.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VClipVolumeOutputs`).
    """
    params = execution.params(params)
    cargs = v__clip_volume_cargs(params, execution)
    ret = v__clip_volume_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__clip_volume(
    input_volume: InputPathType,
    below_zmm: float | None = None,
    above_zmm: float | None = None,
    left_xmm: float | None = None,
    right_xmm: float | None = None,
    anterior_ymm: float | None = None,
    posterior_ymm: float | None = None,
    box: list[float] | None = None,
    mask_box: list[float] | None = None,
    and_logic: bool = False,
    or_logic: bool = False,
    verbosity: bool = False,
    crop_allzero: bool = False,
    crop_greedy: bool = False,
    crop: bool = False,
    crop_npad: float | None = None,
    output_prefix: str | None = None,
    followers: list[InputPathType] | None = None,
    runner: Runner | None = None,
) -> VClipVolumeOutputs:
    """
    A tool to clip regions of a volume in various ways, such as above/below certain
    coordinates or within a specified box.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_volume: Volume to clip.
        below_zmm: Set to 0 slices below Zmm.
        above_zmm: Set to 0 slices above Zmm.
        left_xmm: Set to 0 slices left of Xmm.
        right_xmm: Set to 0 slices right of Xmm.
        anterior_ymm: Set to 0 slices anterior to Ymm.
        posterior_ymm: Set to 0 slices posterior to Ymm.
        box: Clip the volume to a box centered at Cx, Cy, Cz (RAI mm), and of\
            dimensions Dx Dy Dz (RAI mm).
        mask_box: Set all values inside the box to 1. Box centered at Cx, Cy,\
            Cz (RAI mm), and of dimensions Dx Dy Dz (RAI mm).
        and_logic: Combine with next clipping planes using 'and'.
        or_logic: Combine with next clipping planes using 'or'.
        verbosity: Show command details (verbose output).
        crop_allzero: Crop the output volume with 3dAutobox -noclust.
        crop_greedy: Crop the output volume with 3dAutobox.
        crop: Same as -crop_greedy, kept for backward compatibility.
        crop_npad: Set 3dAutobox's -npad option to NPAD. NPAD fattens the\
            volume a little after cropping.
        output_prefix: Output prefix for the resultant volume. Default is the\
            input prefix with _clp suffixed to it.
        followers: Apply the same clipping or cropping treatment to the\
            follower datasets.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VClipVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CLIP_VOLUME_METADATA)
    params = v__clip_volume_params(
        input_volume=input_volume,
        below_zmm=below_zmm,
        above_zmm=above_zmm,
        left_xmm=left_xmm,
        right_xmm=right_xmm,
        anterior_ymm=anterior_ymm,
        posterior_ymm=posterior_ymm,
        box=box,
        mask_box=mask_box,
        and_logic=and_logic,
        or_logic=or_logic,
        verbosity=verbosity,
        crop_allzero=crop_allzero,
        crop_greedy=crop_greedy,
        crop=crop,
        crop_npad=crop_npad,
        output_prefix=output_prefix,
        followers=followers,
    )
    return v__clip_volume_execute(params, execution)


__all__ = [
    "VClipVolumeOutputs",
    "VClipVolumeParameters",
    "V__CLIP_VOLUME_METADATA",
    "v__clip_volume",
    "v__clip_volume_params",
]
