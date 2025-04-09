# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__DJUNCT_OVERLAP_CHECK_METADATA = Metadata(
    id="a8443d34f687d1b2ea3ba63dfe89d00208145343.boutiques",
    name="@djunct_overlap_check",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VDjunctOverlapCheckParameters = typing.TypedDict('VDjunctOverlapCheckParameters', {
    "__STYX_TYPE__": typing.Literal["@djunct_overlap_check"],
    "ulay": InputPathType,
    "olay": InputPathType,
    "prefix": str,
    "box_focus_slices": typing.NotRequired[InputPathType | None],
    "montgap": typing.NotRequired[float | None],
    "montcolor": typing.NotRequired[str | None],
    "cbar": typing.NotRequired[str | None],
    "opacity": typing.NotRequired[float | None],
    "zerocolor": typing.NotRequired[str | None],
    "set_dicom_xyz": typing.NotRequired[list[float] | None],
    "ulay_range": typing.NotRequired[list[float] | None],
    "ulay_range_nz": typing.NotRequired[list[float] | None],
    "montx": typing.NotRequired[float | None],
    "monty": typing.NotRequired[float | None],
    "montx_cat": typing.NotRequired[float | None],
    "monty_cat": typing.NotRequired[float | None],
    "label_mode": typing.NotRequired[str | None],
    "pbar_posonly_off": bool,
    "edgy_ulay": bool,
    "set_dicom_xyz_off": bool,
    "no_cor": bool,
    "no_axi": bool,
    "no_sag": bool,
    "no_clean": bool,
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
        "@djunct_overlap_check": v__djunct_overlap_check_cargs,
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
    }.get(t)


class VDjunctOverlapCheckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__djunct_overlap_check(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__djunct_overlap_check_params(
    ulay: InputPathType,
    olay: InputPathType,
    prefix: str,
    box_focus_slices: InputPathType | None = None,
    montgap: float | None = None,
    montcolor: str | None = None,
    cbar: str | None = None,
    opacity: float | None = None,
    zerocolor: str | None = None,
    set_dicom_xyz: list[float] | None = None,
    ulay_range: list[float] | None = None,
    ulay_range_nz: list[float] | None = None,
    montx: float | None = None,
    monty: float | None = None,
    montx_cat: float | None = None,
    monty_cat: float | None = None,
    label_mode: str | None = None,
    pbar_posonly_off: bool = False,
    edgy_ulay: bool = False,
    set_dicom_xyz_off: bool = False,
    no_cor: bool = False,
    no_axi: bool = False,
    no_sag: bool = False,
    no_clean: bool = False,
) -> VDjunctOverlapCheckParameters:
    """
    Build parameters.
    
    Args:
        ulay: Dataset to use as the underlay (background).
        olay: Dataset to use as the overlay (foreground).
        prefix: Prefix for the output files.
        box_focus_slices: Dataset for box focus slices.
        montgap: Gap between montage slices.
        montcolor: Color of the montage gap.
        cbar: Colorbar for the overlay.
        opacity: Opacity of the overlay.
        zerocolor: Color for zero values.
        set_dicom_xyz: Set DICOM coordinates for slice location.
        ulay_range: Range for underlay values.
        ulay_range_nz: Range for non-zero underlay values.
        montx: Number of panels in X direction in montage.
        monty: Number of panels in Y direction in montage.
        montx_cat: Number of X panes per image in montage.
        monty_cat: Number of Y panes per image in montage.
        label_mode: Label mode.
        pbar_posonly_off: Turn off position-only p-bar.
        edgy_ulay: Edgify the underlay.
        set_dicom_xyz_off: Turn off DICOM coordinates setting.
        no_cor: Skip coronal slices.
        no_axi: Skip axial slices.
        no_sag: Skip sagittal slices.
        no_clean: Do not clean up temporary files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@djunct_overlap_check",
        "ulay": ulay,
        "olay": olay,
        "prefix": prefix,
        "pbar_posonly_off": pbar_posonly_off,
        "edgy_ulay": edgy_ulay,
        "set_dicom_xyz_off": set_dicom_xyz_off,
        "no_cor": no_cor,
        "no_axi": no_axi,
        "no_sag": no_sag,
        "no_clean": no_clean,
    }
    if box_focus_slices is not None:
        params["box_focus_slices"] = box_focus_slices
    if montgap is not None:
        params["montgap"] = montgap
    if montcolor is not None:
        params["montcolor"] = montcolor
    if cbar is not None:
        params["cbar"] = cbar
    if opacity is not None:
        params["opacity"] = opacity
    if zerocolor is not None:
        params["zerocolor"] = zerocolor
    if set_dicom_xyz is not None:
        params["set_dicom_xyz"] = set_dicom_xyz
    if ulay_range is not None:
        params["ulay_range"] = ulay_range
    if ulay_range_nz is not None:
        params["ulay_range_nz"] = ulay_range_nz
    if montx is not None:
        params["montx"] = montx
    if monty is not None:
        params["monty"] = monty
    if montx_cat is not None:
        params["montx_cat"] = montx_cat
    if monty_cat is not None:
        params["monty_cat"] = monty_cat
    if label_mode is not None:
        params["label_mode"] = label_mode
    return params


def v__djunct_overlap_check_cargs(
    params: VDjunctOverlapCheckParameters,
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
    cargs.append("@djunct_overlap_check")
    cargs.append(execution.input_file(params.get("ulay")))
    cargs.append(execution.input_file(params.get("olay")))
    cargs.append(params.get("prefix"))
    if params.get("box_focus_slices") is not None:
        cargs.append(execution.input_file(params.get("box_focus_slices")))
    if params.get("montgap") is not None:
        cargs.extend([
            "-montgap",
            str(params.get("montgap"))
        ])
    if params.get("montcolor") is not None:
        cargs.extend([
            "-montcolor",
            params.get("montcolor")
        ])
    if params.get("cbar") is not None:
        cargs.extend([
            "-cbar",
            params.get("cbar")
        ])
    if params.get("opacity") is not None:
        cargs.extend([
            "-opacity",
            str(params.get("opacity"))
        ])
    if params.get("zerocolor") is not None:
        cargs.extend([
            "-zerocolor",
            params.get("zerocolor")
        ])
    if params.get("set_dicom_xyz") is not None:
        cargs.extend([
            "-set_dicom_xyz",
            *map(str, params.get("set_dicom_xyz"))
        ])
    if params.get("ulay_range") is not None:
        cargs.extend([
            "-ulay_range",
            *map(str, params.get("ulay_range"))
        ])
    if params.get("ulay_range_nz") is not None:
        cargs.extend([
            "-ulay_range_nz",
            *map(str, params.get("ulay_range_nz"))
        ])
    if params.get("montx") is not None:
        cargs.extend([
            "-montx",
            str(params.get("montx"))
        ])
    if params.get("monty") is not None:
        cargs.extend([
            "-monty",
            str(params.get("monty"))
        ])
    if params.get("montx_cat") is not None:
        cargs.extend([
            "-montx_cat",
            str(params.get("montx_cat"))
        ])
    if params.get("monty_cat") is not None:
        cargs.extend([
            "-monty_cat",
            str(params.get("monty_cat"))
        ])
    if params.get("label_mode") is not None:
        cargs.extend([
            "-label_mode",
            params.get("label_mode")
        ])
    if params.get("pbar_posonly_off"):
        cargs.append("-pbar_posonly_off")
    if params.get("edgy_ulay"):
        cargs.append("-edgy_ulay")
    if params.get("set_dicom_xyz_off"):
        cargs.append("-set_dicom_xyz_off")
    if params.get("no_cor"):
        cargs.append("-no_cor")
    if params.get("no_axi"):
        cargs.append("-no_axi")
    if params.get("no_sag"):
        cargs.append("-no_sag")
    if params.get("no_clean"):
        cargs.append("-no_clean")
    return cargs


def v__djunct_overlap_check_outputs(
    params: VDjunctOverlapCheckParameters,
    execution: Execution,
) -> VDjunctOverlapCheckOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VDjunctOverlapCheckOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__djunct_overlap_check_execute(
    params: VDjunctOverlapCheckParameters,
    execution: Execution,
) -> VDjunctOverlapCheckOutputs:
    """
    A helper script for visualizing overlap between datasets in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VDjunctOverlapCheckOutputs`).
    """
    params = execution.params(params)
    cargs = v__djunct_overlap_check_cargs(params, execution)
    ret = v__djunct_overlap_check_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__djunct_overlap_check(
    ulay: InputPathType,
    olay: InputPathType,
    prefix: str,
    box_focus_slices: InputPathType | None = None,
    montgap: float | None = None,
    montcolor: str | None = None,
    cbar: str | None = None,
    opacity: float | None = None,
    zerocolor: str | None = None,
    set_dicom_xyz: list[float] | None = None,
    ulay_range: list[float] | None = None,
    ulay_range_nz: list[float] | None = None,
    montx: float | None = None,
    monty: float | None = None,
    montx_cat: float | None = None,
    monty_cat: float | None = None,
    label_mode: str | None = None,
    pbar_posonly_off: bool = False,
    edgy_ulay: bool = False,
    set_dicom_xyz_off: bool = False,
    no_cor: bool = False,
    no_axi: bool = False,
    no_sag: bool = False,
    no_clean: bool = False,
    runner: Runner | None = None,
) -> VDjunctOverlapCheckOutputs:
    """
    A helper script for visualizing overlap between datasets in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        ulay: Dataset to use as the underlay (background).
        olay: Dataset to use as the overlay (foreground).
        prefix: Prefix for the output files.
        box_focus_slices: Dataset for box focus slices.
        montgap: Gap between montage slices.
        montcolor: Color of the montage gap.
        cbar: Colorbar for the overlay.
        opacity: Opacity of the overlay.
        zerocolor: Color for zero values.
        set_dicom_xyz: Set DICOM coordinates for slice location.
        ulay_range: Range for underlay values.
        ulay_range_nz: Range for non-zero underlay values.
        montx: Number of panels in X direction in montage.
        monty: Number of panels in Y direction in montage.
        montx_cat: Number of X panes per image in montage.
        monty_cat: Number of Y panes per image in montage.
        label_mode: Label mode.
        pbar_posonly_off: Turn off position-only p-bar.
        edgy_ulay: Edgify the underlay.
        set_dicom_xyz_off: Turn off DICOM coordinates setting.
        no_cor: Skip coronal slices.
        no_axi: Skip axial slices.
        no_sag: Skip sagittal slices.
        no_clean: Do not clean up temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDjunctOverlapCheckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DJUNCT_OVERLAP_CHECK_METADATA)
    params = v__djunct_overlap_check_params(
        ulay=ulay,
        olay=olay,
        prefix=prefix,
        box_focus_slices=box_focus_slices,
        montgap=montgap,
        montcolor=montcolor,
        cbar=cbar,
        opacity=opacity,
        zerocolor=zerocolor,
        set_dicom_xyz=set_dicom_xyz,
        ulay_range=ulay_range,
        ulay_range_nz=ulay_range_nz,
        montx=montx,
        monty=monty,
        montx_cat=montx_cat,
        monty_cat=monty_cat,
        label_mode=label_mode,
        pbar_posonly_off=pbar_posonly_off,
        edgy_ulay=edgy_ulay,
        set_dicom_xyz_off=set_dicom_xyz_off,
        no_cor=no_cor,
        no_axi=no_axi,
        no_sag=no_sag,
        no_clean=no_clean,
    )
    return v__djunct_overlap_check_execute(params, execution)


__all__ = [
    "VDjunctOverlapCheckOutputs",
    "VDjunctOverlapCheckParameters",
    "V__DJUNCT_OVERLAP_CHECK_METADATA",
    "v__djunct_overlap_check",
    "v__djunct_overlap_check_params",
]
