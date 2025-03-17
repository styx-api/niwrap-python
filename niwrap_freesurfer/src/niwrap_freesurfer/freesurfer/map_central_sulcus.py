# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MAP_CENTRAL_SULCUS_METADATA = Metadata(
    id="516b76e8b1ac8749a680661e63215cc41d8c82f4.boutiques",
    name="map_central_sulcus",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MapCentralSulcusParameters = typing.TypedDict('MapCentralSulcusParameters', {
    "__STYX_TYPE__": typing.Literal["map_central_sulcus"],
    "subjid": str,
    "process_directive": str,
    "hemi_flag": typing.NotRequired[str | None],
    "expert_prefs_file": typing.NotRequired[InputPathType | None],
    "xopts_use": bool,
    "xopts_clean": bool,
    "xopts_overwrite": bool,
    "watershed_cmd": typing.NotRequired[str | None],
    "xmask_file": typing.NotRequired[InputPathType | None],
    "wsless": bool,
    "wsmore": bool,
    "wsatlas": bool,
    "no_wsatlas": bool,
    "no_wsgcaatlas": bool,
    "wsthresh": typing.NotRequired[float | None],
    "wsseed": typing.NotRequired[str | None],
    "norm3diters": typing.NotRequired[float | None],
    "normmaxgrad": typing.NotRequired[float | None],
    "norm1_b": typing.NotRequired[float | None],
    "norm2_b": typing.NotRequired[float | None],
    "norm1_n": typing.NotRequired[float | None],
    "norm2_n": typing.NotRequired[float | None],
    "cm_flag": bool,
    "no_fix_with_ga": bool,
    "fix_diag_only": bool,
    "seg_wlo": typing.NotRequired[float | None],
    "seg_ghi": typing.NotRequired[float | None],
    "nothicken": bool,
    "no_ca_align_after": bool,
    "no_ca_align": bool,
    "deface": bool,
    "mprage": bool,
    "washu_mprage": bool,
    "schwartzya3t_atlas": bool,
    "mail_username": typing.NotRequired[str | None],
    "threads": typing.NotRequired[float | None],
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
        "map_central_sulcus": map_central_sulcus_cargs,
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
        "map_central_sulcus": map_central_sulcus_outputs,
    }.get(t)


class MapCentralSulcusOutputs(typing.NamedTuple):
    """
    Output object returned when calling `map_central_sulcus(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    log_file: OutputPathType
    """Log file from recon-all process."""
    status_log_file: OutputPathType
    """Status log file from recon-all process."""


def map_central_sulcus_params(
    subjid: str,
    process_directive: str,
    hemi_flag: str | None = None,
    expert_prefs_file: InputPathType | None = None,
    xopts_use: bool = False,
    xopts_clean: bool = False,
    xopts_overwrite: bool = False,
    watershed_cmd: str | None = None,
    xmask_file: InputPathType | None = None,
    wsless: bool = False,
    wsmore: bool = False,
    wsatlas: bool = False,
    no_wsatlas: bool = False,
    no_wsgcaatlas: bool = False,
    wsthresh: float | None = None,
    wsseed: str | None = None,
    norm3diters: float | None = None,
    normmaxgrad: float | None = None,
    norm1_b: float | None = None,
    norm2_b: float | None = None,
    norm1_n: float | None = None,
    norm2_n: float | None = None,
    cm_flag: bool = False,
    no_fix_with_ga: bool = False,
    fix_diag_only: bool = False,
    seg_wlo: float | None = None,
    seg_ghi: float | None = None,
    nothicken: bool = False,
    no_ca_align_after: bool = False,
    no_ca_align: bool = False,
    deface: bool = False,
    mprage: bool = False,
    washu_mprage: bool = False,
    schwartzya3t_atlas: bool = False,
    mail_username: str | None = None,
    threads: float | None = None,
) -> MapCentralSulcusParameters:
    """
    Build parameters.
    
    Args:
        subjid: FreeSurfer subject identification string which doubles as the\
            name of the reconstruction root directory for the subject.
        process_directive: Process directive for recon-all (e.g. -all,\
            -autorecon-all, -autorecon1).
        hemi_flag: Specify hemisphere processing (e.g., lh for left hemisphere\
            or rh for right hemisphere).
        expert_prefs_file: Read-in expert options file for processing.\
            Overrides default options.
        xopts_use: Use pre-existing expert options file.
        xopts_clean: Delete pre-existing expert options file.
        xopts_overwrite: Overwrite pre-existing expert options file.
        watershed_cmd: Controls how the skull stripping will be performed.
        xmask_file: Custom external brain mask to replace automated\
            skullstripping.
        wsless: Decrease watershed threshold (leaves less skull, but can strip\
            more brain).
        wsmore: Increase watershed threshold (leaves more skull, but can strip\
            less brain).
        wsatlas: Use atlas when skull stripping.
        no_wsatlas: Do not use atlas when skull stripping.
        no_wsgcaatlas: Do not use GCA atlas when skull stripping.
        wsthresh: Explicitly set watershed threshold.
        wsseed: Specify an index (C, R, S) point in the skull.
        norm3diters: Number of 3d iterations for mri_normalize.
        normmaxgrad: Max grad (-g) for mri_normalize. Default is 1.
        norm1_b: In the first usage of mri_normalize, use control point with\
            intensity N below target (default=10.0).
        norm2_b: In the second usage of mri_normalize, use control point with\
            intensity N below target (default=10.0).
        norm1_n: In the first usage of mri_normalize, do N number of\
            iterations.
        norm2_n: In the second usage of mri_normalize, do N number of\
            iterations.
        cm_flag: Conform volumes to the min voxel size.
        no_fix_with_ga: Do not use genetic algorithm when fixing topology.
        fix_diag_only: Topology fixer runs until ?h.defect_labels files are\
            created, then stops.
        seg_wlo: Set wlo value for mri_segment and mris_make_surfaces.
        seg_ghi: Set ghi value for mri_segment and mris_make_surfaces.
        nothicken: Pass '-thicken 0' to mri_segment.
        no_ca_align_after: Turn off -align-after with mri_ca_register.
        no_ca_align: Turn off -align with mri_ca_label.
        deface: Deface subject, written to orig_defaced.mgz.
        mprage: Assume scan parameters are MGH MP-RAGE protocol.
        washu_mprage: Assume scan parameters are Wash.U. MP-RAGE protocol.
        schwartzya3t_atlas: For tal reg, use special young adult 3T atlas.
        mail_username: Mail user when done.
        threads: Set number of threads to use.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "map_central_sulcus",
        "subjid": subjid,
        "process_directive": process_directive,
        "xopts_use": xopts_use,
        "xopts_clean": xopts_clean,
        "xopts_overwrite": xopts_overwrite,
        "wsless": wsless,
        "wsmore": wsmore,
        "wsatlas": wsatlas,
        "no_wsatlas": no_wsatlas,
        "no_wsgcaatlas": no_wsgcaatlas,
        "cm_flag": cm_flag,
        "no_fix_with_ga": no_fix_with_ga,
        "fix_diag_only": fix_diag_only,
        "nothicken": nothicken,
        "no_ca_align_after": no_ca_align_after,
        "no_ca_align": no_ca_align,
        "deface": deface,
        "mprage": mprage,
        "washu_mprage": washu_mprage,
        "schwartzya3t_atlas": schwartzya3t_atlas,
    }
    if hemi_flag is not None:
        params["hemi_flag"] = hemi_flag
    if expert_prefs_file is not None:
        params["expert_prefs_file"] = expert_prefs_file
    if watershed_cmd is not None:
        params["watershed_cmd"] = watershed_cmd
    if xmask_file is not None:
        params["xmask_file"] = xmask_file
    if wsthresh is not None:
        params["wsthresh"] = wsthresh
    if wsseed is not None:
        params["wsseed"] = wsseed
    if norm3diters is not None:
        params["norm3diters"] = norm3diters
    if normmaxgrad is not None:
        params["normmaxgrad"] = normmaxgrad
    if norm1_b is not None:
        params["norm1_b"] = norm1_b
    if norm2_b is not None:
        params["norm2_b"] = norm2_b
    if norm1_n is not None:
        params["norm1_n"] = norm1_n
    if norm2_n is not None:
        params["norm2_n"] = norm2_n
    if seg_wlo is not None:
        params["seg_wlo"] = seg_wlo
    if seg_ghi is not None:
        params["seg_ghi"] = seg_ghi
    if mail_username is not None:
        params["mail_username"] = mail_username
    if threads is not None:
        params["threads"] = threads
    return params


def map_central_sulcus_cargs(
    params: MapCentralSulcusParameters,
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
    cargs.append("map_central_sulcus")
    cargs.extend([
        "-subjid",
        params.get("subjid")
    ])
    cargs.append(params.get("process_directive"))
    if params.get("hemi_flag") is not None:
        cargs.extend([
            "-hemi",
            params.get("hemi_flag")
        ])
    if params.get("expert_prefs_file") is not None:
        cargs.extend([
            "-expert",
            execution.input_file(params.get("expert_prefs_file"))
        ])
    if params.get("xopts_use"):
        cargs.append("-xopts-use")
    if params.get("xopts_clean"):
        cargs.append("-xopts-clean")
    if params.get("xopts_overwrite"):
        cargs.append("-xopts-overwrite")
    if params.get("watershed_cmd") is not None:
        cargs.extend([
            "-watershed",
            params.get("watershed_cmd")
        ])
    if params.get("xmask_file") is not None:
        cargs.extend([
            "-xmask",
            execution.input_file(params.get("xmask_file"))
        ])
    if params.get("wsless"):
        cargs.append("-wsless")
    if params.get("wsmore"):
        cargs.append("-wsmore")
    if params.get("wsatlas"):
        cargs.append("-wsatlas")
    if params.get("no_wsatlas"):
        cargs.append("-no-wsatlas")
    if params.get("no_wsgcaatlas"):
        cargs.append("-no-wsgcaatlas")
    if params.get("wsthresh") is not None:
        cargs.extend([
            "-wsthresh",
            str(params.get("wsthresh"))
        ])
    if params.get("wsseed") is not None:
        cargs.extend([
            "-wsseed",
            params.get("wsseed")
        ])
    if params.get("norm3diters") is not None:
        cargs.extend([
            "-norm3diters",
            str(params.get("norm3diters"))
        ])
    if params.get("normmaxgrad") is not None:
        cargs.extend([
            "-normmaxgrad",
            str(params.get("normmaxgrad"))
        ])
    if params.get("norm1_b") is not None:
        cargs.extend([
            "-norm1-b",
            str(params.get("norm1_b"))
        ])
    if params.get("norm2_b") is not None:
        cargs.extend([
            "-norm2-b",
            str(params.get("norm2_b"))
        ])
    if params.get("norm1_n") is not None:
        cargs.extend([
            "-norm1-n",
            str(params.get("norm1_n"))
        ])
    if params.get("norm2_n") is not None:
        cargs.extend([
            "-norm2-n",
            str(params.get("norm2_n"))
        ])
    if params.get("cm_flag"):
        cargs.append("-cm")
    if params.get("no_fix_with_ga"):
        cargs.append("-no-fix-with-ga")
    if params.get("fix_diag_only"):
        cargs.append("-fix-diag-only")
    if params.get("seg_wlo") is not None:
        cargs.extend([
            "-seg-wlo",
            str(params.get("seg_wlo"))
        ])
    if params.get("seg_ghi") is not None:
        cargs.extend([
            "-seg-ghi",
            str(params.get("seg_ghi"))
        ])
    if params.get("nothicken"):
        cargs.append("-nothicken")
    if params.get("no_ca_align_after"):
        cargs.append("-no-ca-align-after")
    if params.get("no_ca_align"):
        cargs.append("-no-ca-align")
    if params.get("deface"):
        cargs.append("-deface")
    if params.get("mprage"):
        cargs.append("-mprage")
    if params.get("washu_mprage"):
        cargs.append("-washu_mprage")
    if params.get("schwartzya3t_atlas"):
        cargs.append("-schwartzya3t-atlas")
    if params.get("mail_username") is not None:
        cargs.extend([
            "-mail",
            params.get("mail_username")
        ])
    if params.get("threads") is not None:
        cargs.extend([
            "-threads",
            str(params.get("threads"))
        ])
    return cargs


def map_central_sulcus_outputs(
    params: MapCentralSulcusParameters,
    execution: Execution,
) -> MapCentralSulcusOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MapCentralSulcusOutputs(
        root=execution.output_file("."),
        log_file=execution.output_file(params.get("subjid") + "/scripts/recon-all.log"),
        status_log_file=execution.output_file(params.get("subjid") + "/scripts/recon-all-status.log"),
    )
    return ret


def map_central_sulcus_execute(
    params: MapCentralSulcusParameters,
    execution: Execution,
) -> MapCentralSulcusOutputs:
    """
    Performs all, or any part of, the FreeSurfer cortical reconstruction process.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MapCentralSulcusOutputs`).
    """
    params = execution.params(params)
    cargs = map_central_sulcus_cargs(params, execution)
    ret = map_central_sulcus_outputs(params, execution)
    execution.run(cargs)
    return ret


def map_central_sulcus(
    subjid: str,
    process_directive: str,
    hemi_flag: str | None = None,
    expert_prefs_file: InputPathType | None = None,
    xopts_use: bool = False,
    xopts_clean: bool = False,
    xopts_overwrite: bool = False,
    watershed_cmd: str | None = None,
    xmask_file: InputPathType | None = None,
    wsless: bool = False,
    wsmore: bool = False,
    wsatlas: bool = False,
    no_wsatlas: bool = False,
    no_wsgcaatlas: bool = False,
    wsthresh: float | None = None,
    wsseed: str | None = None,
    norm3diters: float | None = None,
    normmaxgrad: float | None = None,
    norm1_b: float | None = None,
    norm2_b: float | None = None,
    norm1_n: float | None = None,
    norm2_n: float | None = None,
    cm_flag: bool = False,
    no_fix_with_ga: bool = False,
    fix_diag_only: bool = False,
    seg_wlo: float | None = None,
    seg_ghi: float | None = None,
    nothicken: bool = False,
    no_ca_align_after: bool = False,
    no_ca_align: bool = False,
    deface: bool = False,
    mprage: bool = False,
    washu_mprage: bool = False,
    schwartzya3t_atlas: bool = False,
    mail_username: str | None = None,
    threads: float | None = None,
    runner: Runner | None = None,
) -> MapCentralSulcusOutputs:
    """
    Performs all, or any part of, the FreeSurfer cortical reconstruction process.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjid: FreeSurfer subject identification string which doubles as the\
            name of the reconstruction root directory for the subject.
        process_directive: Process directive for recon-all (e.g. -all,\
            -autorecon-all, -autorecon1).
        hemi_flag: Specify hemisphere processing (e.g., lh for left hemisphere\
            or rh for right hemisphere).
        expert_prefs_file: Read-in expert options file for processing.\
            Overrides default options.
        xopts_use: Use pre-existing expert options file.
        xopts_clean: Delete pre-existing expert options file.
        xopts_overwrite: Overwrite pre-existing expert options file.
        watershed_cmd: Controls how the skull stripping will be performed.
        xmask_file: Custom external brain mask to replace automated\
            skullstripping.
        wsless: Decrease watershed threshold (leaves less skull, but can strip\
            more brain).
        wsmore: Increase watershed threshold (leaves more skull, but can strip\
            less brain).
        wsatlas: Use atlas when skull stripping.
        no_wsatlas: Do not use atlas when skull stripping.
        no_wsgcaatlas: Do not use GCA atlas when skull stripping.
        wsthresh: Explicitly set watershed threshold.
        wsseed: Specify an index (C, R, S) point in the skull.
        norm3diters: Number of 3d iterations for mri_normalize.
        normmaxgrad: Max grad (-g) for mri_normalize. Default is 1.
        norm1_b: In the first usage of mri_normalize, use control point with\
            intensity N below target (default=10.0).
        norm2_b: In the second usage of mri_normalize, use control point with\
            intensity N below target (default=10.0).
        norm1_n: In the first usage of mri_normalize, do N number of\
            iterations.
        norm2_n: In the second usage of mri_normalize, do N number of\
            iterations.
        cm_flag: Conform volumes to the min voxel size.
        no_fix_with_ga: Do not use genetic algorithm when fixing topology.
        fix_diag_only: Topology fixer runs until ?h.defect_labels files are\
            created, then stops.
        seg_wlo: Set wlo value for mri_segment and mris_make_surfaces.
        seg_ghi: Set ghi value for mri_segment and mris_make_surfaces.
        nothicken: Pass '-thicken 0' to mri_segment.
        no_ca_align_after: Turn off -align-after with mri_ca_register.
        no_ca_align: Turn off -align with mri_ca_label.
        deface: Deface subject, written to orig_defaced.mgz.
        mprage: Assume scan parameters are MGH MP-RAGE protocol.
        washu_mprage: Assume scan parameters are Wash.U. MP-RAGE protocol.
        schwartzya3t_atlas: For tal reg, use special young adult 3T atlas.
        mail_username: Mail user when done.
        threads: Set number of threads to use.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MapCentralSulcusOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAP_CENTRAL_SULCUS_METADATA)
    params = map_central_sulcus_params(
        subjid=subjid,
        process_directive=process_directive,
        hemi_flag=hemi_flag,
        expert_prefs_file=expert_prefs_file,
        xopts_use=xopts_use,
        xopts_clean=xopts_clean,
        xopts_overwrite=xopts_overwrite,
        watershed_cmd=watershed_cmd,
        xmask_file=xmask_file,
        wsless=wsless,
        wsmore=wsmore,
        wsatlas=wsatlas,
        no_wsatlas=no_wsatlas,
        no_wsgcaatlas=no_wsgcaatlas,
        wsthresh=wsthresh,
        wsseed=wsseed,
        norm3diters=norm3diters,
        normmaxgrad=normmaxgrad,
        norm1_b=norm1_b,
        norm2_b=norm2_b,
        norm1_n=norm1_n,
        norm2_n=norm2_n,
        cm_flag=cm_flag,
        no_fix_with_ga=no_fix_with_ga,
        fix_diag_only=fix_diag_only,
        seg_wlo=seg_wlo,
        seg_ghi=seg_ghi,
        nothicken=nothicken,
        no_ca_align_after=no_ca_align_after,
        no_ca_align=no_ca_align,
        deface=deface,
        mprage=mprage,
        washu_mprage=washu_mprage,
        schwartzya3t_atlas=schwartzya3t_atlas,
        mail_username=mail_username,
        threads=threads,
    )
    return map_central_sulcus_execute(params, execution)


__all__ = [
    "MAP_CENTRAL_SULCUS_METADATA",
    "MapCentralSulcusOutputs",
    "MapCentralSulcusParameters",
    "map_central_sulcus",
    "map_central_sulcus_params",
]
