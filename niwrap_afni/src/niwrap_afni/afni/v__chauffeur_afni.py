# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__CHAUFFEUR_AFNI_METADATA = Metadata(
    id="bc08654e6aa625d08a0f74755d9ce62b685e3cec.boutiques",
    name="@chauffeur_afni",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VChauffeurAfniParameters = typing.TypedDict('VChauffeurAfniParameters', {
    "__STYXTYPE__": typing.Literal["@chauffeur_afni"],
    "ulay": InputPathType,
    "olay": typing.NotRequired[InputPathType | None],
    "prefix": str,
    "mode_4D": bool,
    "func_range": typing.NotRequired[float | None],
    "opacity": typing.NotRequired[float | None],
    "set_subbricks": typing.NotRequired[str | None],
    "montx": typing.NotRequired[float | None],
    "monty": typing.NotRequired[float | None],
    "montgap": typing.NotRequired[float | None],
    "label_mode": typing.NotRequired[float | None],
    "label_size": typing.NotRequired[float | None],
    "label_color": typing.NotRequired[str | None],
    "label_setback": typing.NotRequired[float | None],
    "no_clean": bool,
    "do_clean": bool,
    "help": bool,
    "version": bool,
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
        "@chauffeur_afni": v__chauffeur_afni_cargs,
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
        "@chauffeur_afni": v__chauffeur_afni_outputs,
    }.get(t)


class VChauffeurAfniOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__chauffeur_afni(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """Generated montage image"""
    cluster_report: OutputPathType
    """Clusterization report"""
    whereami_report: OutputPathType
    """Whereami report for clusterized data"""


def v__chauffeur_afni_params(
    ulay: InputPathType,
    prefix: str,
    olay: InputPathType | None = None,
    mode_4_d: bool = False,
    func_range: float | None = None,
    opacity: float | None = None,
    set_subbricks: str | None = None,
    montx: float | None = None,
    monty: float | None = None,
    montgap: float | None = None,
    label_mode: float | None = None,
    label_size: float | None = None,
    label_color: str | None = None,
    label_setback: float | None = None,
    no_clean: bool = False,
    do_clean: bool = False,
    help_: bool = False,
    version: bool = False,
) -> VChauffeurAfniParameters:
    """
    Build parameters.
    
    Args:
        ulay: Name of underlay dataset (required); can be 3D or 4D set.
        prefix: Prefix for output files (required).
        olay: Name of overlay dataset (optional).
        mode_4_d: For each viewing plane, one slice is selected across all\
            volumes in a 4D dataset.
        func_range: Specify upper value of the overlay dataset to be matched to\
            top of colorbar (default: 98%ile non-zero value of dataset).
        opacity: Enter an opacity factor for the overlay (0-9, with 9 being\
            opaque).
        set_subbricks: Specify subbricks for 3D image viewing.
        montx: Number of image panels in a row (default: 3).
        monty: Number of image panels in a column (default: 3).
        montgap: Number of pixels as gap between image panels (default: 0).
        label_mode: Control labels, ON/OFF and location (default: 1).
        label_size: Control labels, size (default: 3).
        label_color: Control labels, color (default: white).
        label_setback: Control labels, offset from edge (default: 0.01).
        no_clean: Do not remove the temporary directory of copied/intermediate\
            files.
        do_clean: Remove the temporary directory of copied/intermediate files.
        help_: Display help information.
        version: Display version number.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@chauffeur_afni",
        "ulay": ulay,
        "prefix": prefix,
        "mode_4D": mode_4_d,
        "no_clean": no_clean,
        "do_clean": do_clean,
        "help": help_,
        "version": version,
    }
    if olay is not None:
        params["olay"] = olay
    if func_range is not None:
        params["func_range"] = func_range
    if opacity is not None:
        params["opacity"] = opacity
    if set_subbricks is not None:
        params["set_subbricks"] = set_subbricks
    if montx is not None:
        params["montx"] = montx
    if monty is not None:
        params["monty"] = monty
    if montgap is not None:
        params["montgap"] = montgap
    if label_mode is not None:
        params["label_mode"] = label_mode
    if label_size is not None:
        params["label_size"] = label_size
    if label_color is not None:
        params["label_color"] = label_color
    if label_setback is not None:
        params["label_setback"] = label_setback
    return params


def v__chauffeur_afni_cargs(
    params: VChauffeurAfniParameters,
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
    cargs.append("@chauffeur_afni")
    cargs.append(execution.input_file(params.get("ulay")))
    if params.get("olay") is not None:
        cargs.append(execution.input_file(params.get("olay")))
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("mode_4D"):
        cargs.append("-mode_4D")
    if params.get("func_range") is not None:
        cargs.extend([
            "-func_range",
            str(params.get("func_range"))
        ])
    if params.get("opacity") is not None:
        cargs.extend([
            "-opacity",
            str(params.get("opacity"))
        ])
    if params.get("set_subbricks") is not None:
        cargs.extend([
            "-set_subbricks",
            params.get("set_subbricks")
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
    if params.get("montgap") is not None:
        cargs.extend([
            "-montgap",
            str(params.get("montgap"))
        ])
    if params.get("label_mode") is not None:
        cargs.extend([
            "-label_mode",
            str(params.get("label_mode"))
        ])
    if params.get("label_size") is not None:
        cargs.extend([
            "-label_size",
            str(params.get("label_size"))
        ])
    if params.get("label_color") is not None:
        cargs.extend([
            "-label_color",
            params.get("label_color")
        ])
    if params.get("label_setback") is not None:
        cargs.extend([
            "-label_setback",
            str(params.get("label_setback"))
        ])
    if params.get("no_clean"):
        cargs.append("-no_clean")
    if params.get("do_clean"):
        cargs.append("-do_clean")
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-ver")
    return cargs


def v__chauffeur_afni_outputs(
    params: VChauffeurAfniParameters,
    execution: Execution,
) -> VChauffeurAfniOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VChauffeurAfniOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(params.get("prefix") + ".png"),
        cluster_report=execution.output_file(params.get("prefix") + "_clust_rep.txt"),
        whereami_report=execution.output_file(params.get("prefix") + "_clust_whereami.txt"),
    )
    return ret


def v__chauffeur_afni_execute(
    params: VChauffeurAfniParameters,
    execution: Execution,
) -> VChauffeurAfniOutputs:
    """
    Automated QC snapshots generator in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VChauffeurAfniOutputs`).
    """
    params = execution.params(params)
    cargs = v__chauffeur_afni_cargs(params, execution)
    ret = v__chauffeur_afni_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__chauffeur_afni(
    ulay: InputPathType,
    prefix: str,
    olay: InputPathType | None = None,
    mode_4_d: bool = False,
    func_range: float | None = None,
    opacity: float | None = None,
    set_subbricks: str | None = None,
    montx: float | None = None,
    monty: float | None = None,
    montgap: float | None = None,
    label_mode: float | None = None,
    label_size: float | None = None,
    label_color: str | None = None,
    label_setback: float | None = None,
    no_clean: bool = False,
    do_clean: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> VChauffeurAfniOutputs:
    """
    Automated QC snapshots generator in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        ulay: Name of underlay dataset (required); can be 3D or 4D set.
        prefix: Prefix for output files (required).
        olay: Name of overlay dataset (optional).
        mode_4_d: For each viewing plane, one slice is selected across all\
            volumes in a 4D dataset.
        func_range: Specify upper value of the overlay dataset to be matched to\
            top of colorbar (default: 98%ile non-zero value of dataset).
        opacity: Enter an opacity factor for the overlay (0-9, with 9 being\
            opaque).
        set_subbricks: Specify subbricks for 3D image viewing.
        montx: Number of image panels in a row (default: 3).
        monty: Number of image panels in a column (default: 3).
        montgap: Number of pixels as gap between image panels (default: 0).
        label_mode: Control labels, ON/OFF and location (default: 1).
        label_size: Control labels, size (default: 3).
        label_color: Control labels, color (default: white).
        label_setback: Control labels, offset from edge (default: 0.01).
        no_clean: Do not remove the temporary directory of copied/intermediate\
            files.
        do_clean: Remove the temporary directory of copied/intermediate files.
        help_: Display help information.
        version: Display version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VChauffeurAfniOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CHAUFFEUR_AFNI_METADATA)
    params = v__chauffeur_afni_params(
        ulay=ulay,
        olay=olay,
        prefix=prefix,
        mode_4_d=mode_4_d,
        func_range=func_range,
        opacity=opacity,
        set_subbricks=set_subbricks,
        montx=montx,
        monty=monty,
        montgap=montgap,
        label_mode=label_mode,
        label_size=label_size,
        label_color=label_color,
        label_setback=label_setback,
        no_clean=no_clean,
        do_clean=do_clean,
        help_=help_,
        version=version,
    )
    return v__chauffeur_afni_execute(params, execution)


__all__ = [
    "VChauffeurAfniOutputs",
    "VChauffeurAfniParameters",
    "V__CHAUFFEUR_AFNI_METADATA",
    "v__chauffeur_afni",
    "v__chauffeur_afni_params",
]
