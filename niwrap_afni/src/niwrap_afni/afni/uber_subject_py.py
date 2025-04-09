# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

UBER_SUBJECT_PY_METADATA = Metadata(
    id="530df676c8d2b6020a3d36b7074940b4993bef60.boutiques",
    name="uber_subject.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


UberSubjectPyParameters = typing.TypedDict('UberSubjectPyParameters', {
    "__STYX_TYPE__": typing.Literal["uber_subject.py"],
    "qt_opts": typing.NotRequired[str | None],
    "svar": typing.NotRequired[str | None],
    "cvar": typing.NotRequired[str | None],
    "no_gui": bool,
    "print_ap_command": bool,
    "save_ap_command": typing.NotRequired[str | None],
    "exec_ap_command": bool,
    "exec_proc_script": bool,
    "align_cost": typing.NotRequired[str | None],
    "align_giant_move": typing.NotRequired[str | None],
    "align_opts_aea": typing.NotRequired[str | None],
    "anal_domain": typing.NotRequired[str | None],
    "anal_type": typing.NotRequired[str | None],
    "anat": typing.NotRequired[InputPathType | None],
    "anat_has_skull": typing.NotRequired[str | None],
    "blocks": typing.NotRequired[str | None],
    "blur_size": typing.NotRequired[float | None],
    "epi": typing.NotRequired[str | None],
    "epi_wildcard": typing.NotRequired[str | None],
    "gid": typing.NotRequired[str | None],
    "gltsym": typing.NotRequired[str | None],
    "gltsym_label": typing.NotRequired[str | None],
    "motion_limit": typing.NotRequired[float | None],
    "outlier_limit": typing.NotRequired[float | None],
    "regress_GOFORIT": typing.NotRequired[float | None],
    "regress_bandpass": typing.NotRequired[str | None],
    "regress_jobs": typing.NotRequired[float | None],
    "regress_mot_deriv": typing.NotRequired[str | None],
    "regress_opts_3dD": typing.NotRequired[str | None],
    "reml_exec": typing.NotRequired[str | None],
    "run_clustsim": typing.NotRequired[str | None],
    "sid": typing.NotRequired[str | None],
    "stim": typing.NotRequired[InputPathType | None],
    "stim_basis": typing.NotRequired[str | None],
    "stim_label": typing.NotRequired[str | None],
    "stim_type": typing.NotRequired[str | None],
    "stim_wildcard": typing.NotRequired[str | None],
    "tcat_nfirst": typing.NotRequired[float | None],
    "tlrc_base": typing.NotRequired[str | None],
    "tlrc_ok_maxite": typing.NotRequired[str | None],
    "tlrc_opts_at": typing.NotRequired[str | None],
    "volreg_base": typing.NotRequired[str | None],
    "verb": typing.NotRequired[str | None],
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
        "uber_subject.py": uber_subject_py_cargs,
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


class UberSubjectPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `uber_subject_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def uber_subject_py_params(
    qt_opts: str | None = None,
    svar: str | None = None,
    cvar: str | None = None,
    no_gui: bool = False,
    print_ap_command: bool = False,
    save_ap_command: str | None = None,
    exec_ap_command: bool = False,
    exec_proc_script: bool = False,
    align_cost: str | None = None,
    align_giant_move: str | None = None,
    align_opts_aea: str | None = None,
    anal_domain: str | None = None,
    anal_type: str | None = None,
    anat: InputPathType | None = None,
    anat_has_skull: str | None = None,
    blocks: str | None = None,
    blur_size: float | None = None,
    epi: str | None = None,
    epi_wildcard: str | None = None,
    gid: str | None = None,
    gltsym: str | None = None,
    gltsym_label: str | None = None,
    motion_limit: float | None = None,
    outlier_limit: float | None = None,
    regress_goforit: float | None = None,
    regress_bandpass: str | None = None,
    regress_jobs: float | None = None,
    regress_mot_deriv: str | None = None,
    regress_opts_3d_d: str | None = None,
    reml_exec: str | None = None,
    run_clustsim: str | None = None,
    sid: str | None = None,
    stim: InputPathType | None = None,
    stim_basis: str | None = None,
    stim_label: str | None = None,
    stim_type: str | None = None,
    stim_wildcard: str | None = None,
    tcat_nfirst: float | None = None,
    tlrc_base: str | None = None,
    tlrc_ok_maxite: str | None = None,
    tlrc_opts_at: str | None = None,
    volreg_base: str | None = None,
    verb: str | None = None,
) -> UberSubjectPyParameters:
    """
    Build parameters.
    
    Args:
        qt_opts: Pass options to PyQt4.
        svar: Set subject variable to value.
        cvar: Set control variable to value.
        no_gui: Do not open graphical interface.
        print_ap_command: Show afni_proc.py script.
        save_ap_command: Save afni_proc.py script.
        exec_ap_command: Run afni_proc.py command.
        exec_proc_script: Run proc script.
        align_cost: Specify cost function for anat/EPI alignment.
        align_giant_move: Use -giant_move in AEA.py.
        align_opts_aea: Specify extra options for align_epi_anat.py.
        anal_domain: Set data domain (volume/rest).
        anal_type: Set analysis type (task/rest).
        anat: Set anatomical dataset name.
        anat_has_skull: Whether anat has skull (yes/no).
        blocks: Set list of processing blocks to apply.
        blur_size: Set blur size in mm.
        epi: Set list of EPI datasets.
        epi_wildcard: Use wildcard for EPI datasets (yes/no).
        gid: Set group ID.
        gltsym: Specify list of symbolic GLTs.
        gltsym_label: Set corresponding GLT labels.
        motion_limit: Set per-TR motion limit in mm.
        outlier_limit: Specify outlier limit for censoring.
        regress_goforit: Set GOFORIT level in 3dDeconvolve.
        regress_bandpass: Specify bandpass limits to remain after regress.
        regress_jobs: Number of jobs to use in 3dDeconvolve.
        regress_mot_deriv: Regress motion derivatives (yes/no).
        regress_opts_3d_d: Specify extra options for 3dDeconvolve.
        reml_exec: Run 3dREMLfit (yes/no).
        run_clustsim: Run 3dClustSim (yes/no).
        sid: Set subject ID.
        stim: Set list of stim timing files.
        stim_basis: Set basis functions for stim classes.
        stim_label: Set stim file labels.
        stim_type: Set stim types for stim classes.
        stim_wildcard: Use wildcard for stim files (yes/no).
        tcat_nfirst: Set number of TRs to remove per run.
        tlrc_base: Specify anat for standard space alignment.
        tlrc_ok_maxite: Pass -OK_maxite to @auto_tlrc (yes/no).
        tlrc_opts_at: Specify extra options for @auto_tlrc.
        volreg_base: Set volreg base string (first/third/last).
        verb: Set verbose level.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "uber_subject.py",
        "no_gui": no_gui,
        "print_ap_command": print_ap_command,
        "exec_ap_command": exec_ap_command,
        "exec_proc_script": exec_proc_script,
    }
    if qt_opts is not None:
        params["qt_opts"] = qt_opts
    if svar is not None:
        params["svar"] = svar
    if cvar is not None:
        params["cvar"] = cvar
    if save_ap_command is not None:
        params["save_ap_command"] = save_ap_command
    if align_cost is not None:
        params["align_cost"] = align_cost
    if align_giant_move is not None:
        params["align_giant_move"] = align_giant_move
    if align_opts_aea is not None:
        params["align_opts_aea"] = align_opts_aea
    if anal_domain is not None:
        params["anal_domain"] = anal_domain
    if anal_type is not None:
        params["anal_type"] = anal_type
    if anat is not None:
        params["anat"] = anat
    if anat_has_skull is not None:
        params["anat_has_skull"] = anat_has_skull
    if blocks is not None:
        params["blocks"] = blocks
    if blur_size is not None:
        params["blur_size"] = blur_size
    if epi is not None:
        params["epi"] = epi
    if epi_wildcard is not None:
        params["epi_wildcard"] = epi_wildcard
    if gid is not None:
        params["gid"] = gid
    if gltsym is not None:
        params["gltsym"] = gltsym
    if gltsym_label is not None:
        params["gltsym_label"] = gltsym_label
    if motion_limit is not None:
        params["motion_limit"] = motion_limit
    if outlier_limit is not None:
        params["outlier_limit"] = outlier_limit
    if regress_goforit is not None:
        params["regress_GOFORIT"] = regress_goforit
    if regress_bandpass is not None:
        params["regress_bandpass"] = regress_bandpass
    if regress_jobs is not None:
        params["regress_jobs"] = regress_jobs
    if regress_mot_deriv is not None:
        params["regress_mot_deriv"] = regress_mot_deriv
    if regress_opts_3d_d is not None:
        params["regress_opts_3dD"] = regress_opts_3d_d
    if reml_exec is not None:
        params["reml_exec"] = reml_exec
    if run_clustsim is not None:
        params["run_clustsim"] = run_clustsim
    if sid is not None:
        params["sid"] = sid
    if stim is not None:
        params["stim"] = stim
    if stim_basis is not None:
        params["stim_basis"] = stim_basis
    if stim_label is not None:
        params["stim_label"] = stim_label
    if stim_type is not None:
        params["stim_type"] = stim_type
    if stim_wildcard is not None:
        params["stim_wildcard"] = stim_wildcard
    if tcat_nfirst is not None:
        params["tcat_nfirst"] = tcat_nfirst
    if tlrc_base is not None:
        params["tlrc_base"] = tlrc_base
    if tlrc_ok_maxite is not None:
        params["tlrc_ok_maxite"] = tlrc_ok_maxite
    if tlrc_opts_at is not None:
        params["tlrc_opts_at"] = tlrc_opts_at
    if volreg_base is not None:
        params["volreg_base"] = volreg_base
    if verb is not None:
        params["verb"] = verb
    return params


def uber_subject_py_cargs(
    params: UberSubjectPyParameters,
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
    cargs.append("uber_subject.py")
    if params.get("qt_opts") is not None:
        cargs.extend([
            "-qt_opts",
            params.get("qt_opts")
        ])
    if params.get("svar") is not None:
        cargs.extend([
            "-svar",
            params.get("svar")
        ])
    if params.get("cvar") is not None:
        cargs.extend([
            "-cvar",
            params.get("cvar")
        ])
    if params.get("no_gui"):
        cargs.append("-no_gui")
    if params.get("print_ap_command"):
        cargs.append("-print_ap_command")
    if params.get("save_ap_command") is not None:
        cargs.extend([
            "-save_ap_command",
            params.get("save_ap_command")
        ])
    if params.get("exec_ap_command"):
        cargs.append("-exec_ap_command")
    if params.get("exec_proc_script"):
        cargs.append("-exec_proc_script")
    if params.get("align_cost") is not None:
        cargs.extend([
            "-align_cost",
            params.get("align_cost")
        ])
    if params.get("align_giant_move") is not None:
        cargs.extend([
            "-align_giant_move",
            params.get("align_giant_move")
        ])
    if params.get("align_opts_aea") is not None:
        cargs.extend([
            "-align_opts_aea",
            params.get("align_opts_aea")
        ])
    if params.get("anal_domain") is not None:
        cargs.extend([
            "-anal_domain",
            params.get("anal_domain")
        ])
    if params.get("anal_type") is not None:
        cargs.extend([
            "-anal_type",
            params.get("anal_type")
        ])
    if params.get("anat") is not None:
        cargs.extend([
            "-anat",
            execution.input_file(params.get("anat"))
        ])
    if params.get("anat_has_skull") is not None:
        cargs.extend([
            "-anat_has_skull",
            params.get("anat_has_skull")
        ])
    if params.get("blocks") is not None:
        cargs.extend([
            "-blocks",
            params.get("blocks")
        ])
    if params.get("blur_size") is not None:
        cargs.extend([
            "-blur_size",
            str(params.get("blur_size"))
        ])
    if params.get("epi") is not None:
        cargs.extend([
            "-epi",
            params.get("epi")
        ])
    if params.get("epi_wildcard") is not None:
        cargs.extend([
            "-epi_wildcard",
            params.get("epi_wildcard")
        ])
    if params.get("gid") is not None:
        cargs.extend([
            "-gid",
            params.get("gid")
        ])
    if params.get("gltsym") is not None:
        cargs.extend([
            "-gltsym",
            params.get("gltsym")
        ])
    if params.get("gltsym_label") is not None:
        cargs.extend([
            "-gltsym_label",
            params.get("gltsym_label")
        ])
    if params.get("motion_limit") is not None:
        cargs.extend([
            "-motion_limit",
            str(params.get("motion_limit"))
        ])
    if params.get("outlier_limit") is not None:
        cargs.extend([
            "-outlier_limit",
            str(params.get("outlier_limit"))
        ])
    if params.get("regress_GOFORIT") is not None:
        cargs.extend([
            "-regress_GOFORIT",
            str(params.get("regress_GOFORIT"))
        ])
    if params.get("regress_bandpass") is not None:
        cargs.extend([
            "-regress_bandpass",
            params.get("regress_bandpass")
        ])
    if params.get("regress_jobs") is not None:
        cargs.extend([
            "-regress_jobs",
            str(params.get("regress_jobs"))
        ])
    if params.get("regress_mot_deriv") is not None:
        cargs.extend([
            "-regress_mot_deriv",
            params.get("regress_mot_deriv")
        ])
    if params.get("regress_opts_3dD") is not None:
        cargs.extend([
            "-regress_opts_3dD",
            params.get("regress_opts_3dD")
        ])
    if params.get("reml_exec") is not None:
        cargs.extend([
            "-reml_exec",
            params.get("reml_exec")
        ])
    if params.get("run_clustsim") is not None:
        cargs.extend([
            "-run_clustsim",
            params.get("run_clustsim")
        ])
    if params.get("sid") is not None:
        cargs.extend([
            "-sid",
            params.get("sid")
        ])
    if params.get("stim") is not None:
        cargs.extend([
            "-stim",
            execution.input_file(params.get("stim"))
        ])
    if params.get("stim_basis") is not None:
        cargs.extend([
            "-stim_basis",
            params.get("stim_basis")
        ])
    if params.get("stim_label") is not None:
        cargs.extend([
            "-stim_label",
            params.get("stim_label")
        ])
    if params.get("stim_type") is not None:
        cargs.extend([
            "-stim_type",
            params.get("stim_type")
        ])
    if params.get("stim_wildcard") is not None:
        cargs.extend([
            "-stim_wildcard",
            params.get("stim_wildcard")
        ])
    if params.get("tcat_nfirst") is not None:
        cargs.extend([
            "-tcat_nfirst",
            str(params.get("tcat_nfirst"))
        ])
    if params.get("tlrc_base") is not None:
        cargs.extend([
            "-tlrc_base",
            params.get("tlrc_base")
        ])
    if params.get("tlrc_ok_maxite") is not None:
        cargs.extend([
            "-tlrc_ok_maxite",
            params.get("tlrc_ok_maxite")
        ])
    if params.get("tlrc_opts_at") is not None:
        cargs.extend([
            "-tlrc_opts_at",
            params.get("tlrc_opts_at")
        ])
    if params.get("volreg_base") is not None:
        cargs.extend([
            "-volreg_base",
            params.get("volreg_base")
        ])
    if params.get("verb") is not None:
        cargs.extend([
            "-verb",
            params.get("verb")
        ])
    return cargs


def uber_subject_py_outputs(
    params: UberSubjectPyParameters,
    execution: Execution,
) -> UberSubjectPyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = UberSubjectPyOutputs(
        root=execution.output_file("."),
    )
    return ret


def uber_subject_py_execute(
    params: UberSubjectPyParameters,
    execution: Execution,
) -> UberSubjectPyOutputs:
    """
    Graphical interface to afni_proc.py.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `UberSubjectPyOutputs`).
    """
    params = execution.params(params)
    cargs = uber_subject_py_cargs(params, execution)
    ret = uber_subject_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def uber_subject_py(
    qt_opts: str | None = None,
    svar: str | None = None,
    cvar: str | None = None,
    no_gui: bool = False,
    print_ap_command: bool = False,
    save_ap_command: str | None = None,
    exec_ap_command: bool = False,
    exec_proc_script: bool = False,
    align_cost: str | None = None,
    align_giant_move: str | None = None,
    align_opts_aea: str | None = None,
    anal_domain: str | None = None,
    anal_type: str | None = None,
    anat: InputPathType | None = None,
    anat_has_skull: str | None = None,
    blocks: str | None = None,
    blur_size: float | None = None,
    epi: str | None = None,
    epi_wildcard: str | None = None,
    gid: str | None = None,
    gltsym: str | None = None,
    gltsym_label: str | None = None,
    motion_limit: float | None = None,
    outlier_limit: float | None = None,
    regress_goforit: float | None = None,
    regress_bandpass: str | None = None,
    regress_jobs: float | None = None,
    regress_mot_deriv: str | None = None,
    regress_opts_3d_d: str | None = None,
    reml_exec: str | None = None,
    run_clustsim: str | None = None,
    sid: str | None = None,
    stim: InputPathType | None = None,
    stim_basis: str | None = None,
    stim_label: str | None = None,
    stim_type: str | None = None,
    stim_wildcard: str | None = None,
    tcat_nfirst: float | None = None,
    tlrc_base: str | None = None,
    tlrc_ok_maxite: str | None = None,
    tlrc_opts_at: str | None = None,
    volreg_base: str | None = None,
    verb: str | None = None,
    runner: Runner | None = None,
) -> UberSubjectPyOutputs:
    """
    Graphical interface to afni_proc.py.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        qt_opts: Pass options to PyQt4.
        svar: Set subject variable to value.
        cvar: Set control variable to value.
        no_gui: Do not open graphical interface.
        print_ap_command: Show afni_proc.py script.
        save_ap_command: Save afni_proc.py script.
        exec_ap_command: Run afni_proc.py command.
        exec_proc_script: Run proc script.
        align_cost: Specify cost function for anat/EPI alignment.
        align_giant_move: Use -giant_move in AEA.py.
        align_opts_aea: Specify extra options for align_epi_anat.py.
        anal_domain: Set data domain (volume/rest).
        anal_type: Set analysis type (task/rest).
        anat: Set anatomical dataset name.
        anat_has_skull: Whether anat has skull (yes/no).
        blocks: Set list of processing blocks to apply.
        blur_size: Set blur size in mm.
        epi: Set list of EPI datasets.
        epi_wildcard: Use wildcard for EPI datasets (yes/no).
        gid: Set group ID.
        gltsym: Specify list of symbolic GLTs.
        gltsym_label: Set corresponding GLT labels.
        motion_limit: Set per-TR motion limit in mm.
        outlier_limit: Specify outlier limit for censoring.
        regress_goforit: Set GOFORIT level in 3dDeconvolve.
        regress_bandpass: Specify bandpass limits to remain after regress.
        regress_jobs: Number of jobs to use in 3dDeconvolve.
        regress_mot_deriv: Regress motion derivatives (yes/no).
        regress_opts_3d_d: Specify extra options for 3dDeconvolve.
        reml_exec: Run 3dREMLfit (yes/no).
        run_clustsim: Run 3dClustSim (yes/no).
        sid: Set subject ID.
        stim: Set list of stim timing files.
        stim_basis: Set basis functions for stim classes.
        stim_label: Set stim file labels.
        stim_type: Set stim types for stim classes.
        stim_wildcard: Use wildcard for stim files (yes/no).
        tcat_nfirst: Set number of TRs to remove per run.
        tlrc_base: Specify anat for standard space alignment.
        tlrc_ok_maxite: Pass -OK_maxite to @auto_tlrc (yes/no).
        tlrc_opts_at: Specify extra options for @auto_tlrc.
        volreg_base: Set volreg base string (first/third/last).
        verb: Set verbose level.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UberSubjectPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UBER_SUBJECT_PY_METADATA)
    params = uber_subject_py_params(
        qt_opts=qt_opts,
        svar=svar,
        cvar=cvar,
        no_gui=no_gui,
        print_ap_command=print_ap_command,
        save_ap_command=save_ap_command,
        exec_ap_command=exec_ap_command,
        exec_proc_script=exec_proc_script,
        align_cost=align_cost,
        align_giant_move=align_giant_move,
        align_opts_aea=align_opts_aea,
        anal_domain=anal_domain,
        anal_type=anal_type,
        anat=anat,
        anat_has_skull=anat_has_skull,
        blocks=blocks,
        blur_size=blur_size,
        epi=epi,
        epi_wildcard=epi_wildcard,
        gid=gid,
        gltsym=gltsym,
        gltsym_label=gltsym_label,
        motion_limit=motion_limit,
        outlier_limit=outlier_limit,
        regress_goforit=regress_goforit,
        regress_bandpass=regress_bandpass,
        regress_jobs=regress_jobs,
        regress_mot_deriv=regress_mot_deriv,
        regress_opts_3d_d=regress_opts_3d_d,
        reml_exec=reml_exec,
        run_clustsim=run_clustsim,
        sid=sid,
        stim=stim,
        stim_basis=stim_basis,
        stim_label=stim_label,
        stim_type=stim_type,
        stim_wildcard=stim_wildcard,
        tcat_nfirst=tcat_nfirst,
        tlrc_base=tlrc_base,
        tlrc_ok_maxite=tlrc_ok_maxite,
        tlrc_opts_at=tlrc_opts_at,
        volreg_base=volreg_base,
        verb=verb,
    )
    return uber_subject_py_execute(params, execution)


__all__ = [
    "UBER_SUBJECT_PY_METADATA",
    "UberSubjectPyOutputs",
    "UberSubjectPyParameters",
    "uber_subject_py",
    "uber_subject_py_params",
]
