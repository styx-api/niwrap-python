# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TRAC_ALL_METADATA = Metadata(
    id="4b02da6d23bbdf1aadba4f7ad8effbf91cb48ef5.boutiques",
    name="trac-all",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


TracAllParameters = typing.TypedDict('TracAllParameters', {
    "__STYXTYPE__": typing.Literal["trac-all"],
    "config_file": typing.NotRequired[InputPathType | None],
    "subject_name": typing.NotRequired[str | None],
    "dicom_file": typing.NotRequired[InputPathType | None],
    "pre_processing": bool,
    "bedpost": bool,
    "pathway_reconstruction": bool,
    "assemble_measures": bool,
    "image_corrections": bool,
    "no_image_corrections": bool,
    "image_quality_assessment": bool,
    "no_image_quality_assessment": bool,
    "intra_registration": bool,
    "no_intra_registration": bool,
    "tensor_fit": bool,
    "no_tensor_fit": bool,
    "inter_registration": bool,
    "no_inter_registration": bool,
    "pathway_priors": bool,
    "no_pathway_priors": bool,
    "infant_options": bool,
    "job_file": typing.NotRequired[InputPathType | None],
    "log_file": typing.NotRequired[str | None],
    "no_append_log": bool,
    "cmd_file": typing.NotRequired[str | None],
    "no_is_running": bool,
    "subjects_directory": typing.NotRequired[str | None],
    "umask": typing.NotRequired[str | None],
    "group_id": typing.NotRequired[str | None],
    "allow_core_dump": bool,
    "debug_mode": bool,
    "dont_run": bool,
    "only_versions": bool,
    "version_info": bool,
    "help": bool,
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
        "trac-all": trac_all_cargs,
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
        "trac-all": trac_all_outputs,
    }.get(t)


class TracAllOutputs(typing.NamedTuple):
    """
    Output object returned when calling `trac_all(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    default_log: OutputPathType
    """Default log file"""
    default_cmd: OutputPathType
    """Default command file"""


def trac_all_params(
    config_file: InputPathType | None = None,
    subject_name: str | None = None,
    dicom_file: InputPathType | None = None,
    pre_processing: bool = False,
    bedpost: bool = False,
    pathway_reconstruction: bool = False,
    assemble_measures: bool = False,
    image_corrections: bool = False,
    no_image_corrections: bool = False,
    image_quality_assessment: bool = False,
    no_image_quality_assessment: bool = False,
    intra_registration: bool = False,
    no_intra_registration: bool = False,
    tensor_fit: bool = False,
    no_tensor_fit: bool = False,
    inter_registration: bool = False,
    no_inter_registration: bool = False,
    pathway_priors: bool = False,
    no_pathway_priors: bool = False,
    infant_options: bool = False,
    job_file: InputPathType | None = None,
    log_file: str | None = None,
    no_append_log: bool = False,
    cmd_file: str | None = None,
    no_is_running: bool = False,
    subjects_directory: str | None = None,
    umask: str | None = None,
    group_id: str | None = None,
    allow_core_dump: bool = False,
    debug_mode: bool = False,
    dont_run: bool = False,
    only_versions: bool = False,
    version_info: bool = False,
    help_: bool = False,
) -> TracAllParameters:
    """
    Build parameters.
    
    Args:
        config_file: Configuration file to set analysis options (dmrirc file).
        subject_name: Subject name (if not defined in dmrirc).
        dicom_file: Input DWI DICOM (if not defined in dmrirc).
        pre_processing: Perform pre-processing (step 1, all substeps).
        bedpost: Perform bedpost (step 2).
        pathway_reconstruction: Perform pathway reconstruction (step 3).
        assemble_measures: Assemble pathway measures from multiple subjects\
            (step 4).
        image_corrections: Perform image corrections (step 1.1).
        no_image_corrections: Skip image corrections (step 1.1).
        image_quality_assessment: Perform image quality assessment (step 1.2).
        no_image_quality_assessment: Skip image quality assessment (step 1.2).
        intra_registration: Perform intra-subject registration (step 1.3).
        no_intra_registration: Skip intra-subject registration (step 1.3).
        tensor_fit: Perform tensor fit (step 1.4).
        no_tensor_fit: Skip tensor fit (step 1.4).
        inter_registration: Perform inter-subject registration (step 1.5).
        no_inter_registration: Skip inter-subject registration (step 1.5).
        pathway_priors: Perform pathway priors (step 1.6).
        no_pathway_priors: Skip pathway priors (step 1.6).
        infant_options: Use infant brain processing options.
        job_file: Write a text file with command lines that can be run in\
            parallel and do not run them.
        log_file: Unique log file instead of the default scripts/trac-all.log.
        no_append_log: Overwrite old log files instead of appending.
        cmd_file: Unique cmd file instead of the default scripts/trac-all.cmd.
        no_is_running: Do not check whether subjects are currently being\
            processed.
        subjects_directory: Specify subjects directory (default environment\
            SUBJECTS_DIR).
        umask: Set Unix file permission mask (default 002).
        group_id: Check that current group is alpha groupid.
        allow_core_dump: Set coredump limit to unlimited.
        debug_mode: Generate much more output.
        dont_run: Do everything but execute each command.
        only_versions: Print version of each binary and exit.
        version_info: Print version of this script and exit.
        help_: Print full contents of help.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "trac-all",
        "pre_processing": pre_processing,
        "bedpost": bedpost,
        "pathway_reconstruction": pathway_reconstruction,
        "assemble_measures": assemble_measures,
        "image_corrections": image_corrections,
        "no_image_corrections": no_image_corrections,
        "image_quality_assessment": image_quality_assessment,
        "no_image_quality_assessment": no_image_quality_assessment,
        "intra_registration": intra_registration,
        "no_intra_registration": no_intra_registration,
        "tensor_fit": tensor_fit,
        "no_tensor_fit": no_tensor_fit,
        "inter_registration": inter_registration,
        "no_inter_registration": no_inter_registration,
        "pathway_priors": pathway_priors,
        "no_pathway_priors": no_pathway_priors,
        "infant_options": infant_options,
        "no_append_log": no_append_log,
        "no_is_running": no_is_running,
        "allow_core_dump": allow_core_dump,
        "debug_mode": debug_mode,
        "dont_run": dont_run,
        "only_versions": only_versions,
        "version_info": version_info,
        "help": help_,
    }
    if config_file is not None:
        params["config_file"] = config_file
    if subject_name is not None:
        params["subject_name"] = subject_name
    if dicom_file is not None:
        params["dicom_file"] = dicom_file
    if job_file is not None:
        params["job_file"] = job_file
    if log_file is not None:
        params["log_file"] = log_file
    if cmd_file is not None:
        params["cmd_file"] = cmd_file
    if subjects_directory is not None:
        params["subjects_directory"] = subjects_directory
    if umask is not None:
        params["umask"] = umask
    if group_id is not None:
        params["group_id"] = group_id
    return params


def trac_all_cargs(
    params: TracAllParameters,
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
    cargs.append("trac-all")
    if params.get("config_file") is not None:
        cargs.extend([
            "-c",
            execution.input_file(params.get("config_file"))
        ])
    if params.get("subject_name") is not None:
        cargs.extend([
            "-s",
            params.get("subject_name")
        ])
    if params.get("dicom_file") is not None:
        cargs.extend([
            "-i",
            execution.input_file(params.get("dicom_file"))
        ])
    if params.get("pre_processing"):
        cargs.append("-prep")
    if params.get("bedpost"):
        cargs.append("-bedp")
    if params.get("pathway_reconstruction"):
        cargs.append("-path")
    if params.get("assemble_measures"):
        cargs.append("-stat")
    if params.get("image_corrections"):
        cargs.append("-corr")
    if params.get("no_image_corrections"):
        cargs.append("-nocorr")
    if params.get("image_quality_assessment"):
        cargs.append("-qa")
    if params.get("no_image_quality_assessment"):
        cargs.append("-noqa")
    if params.get("intra_registration"):
        cargs.append("-intra")
    if params.get("no_intra_registration"):
        cargs.append("-nointra")
    if params.get("tensor_fit"):
        cargs.append("-tensor")
    if params.get("no_tensor_fit"):
        cargs.append("-notensor")
    if params.get("inter_registration"):
        cargs.append("-inter")
    if params.get("no_inter_registration"):
        cargs.append("-nointer")
    if params.get("pathway_priors"):
        cargs.append("-prior")
    if params.get("no_pathway_priors"):
        cargs.append("-noprior")
    if params.get("infant_options"):
        cargs.append("-infant")
    if params.get("job_file") is not None:
        cargs.extend([
            "-jobs",
            execution.input_file(params.get("job_file"))
        ])
    if params.get("log_file") is not None:
        cargs.extend([
            "-log",
            params.get("log_file")
        ])
    if params.get("no_append_log"):
        cargs.append("-noappendlog")
    if params.get("cmd_file") is not None:
        cargs.extend([
            "-cmd",
            params.get("cmd_file")
        ])
    if params.get("no_is_running"):
        cargs.append("-no-isrunning")
    if params.get("subjects_directory") is not None:
        cargs.extend([
            "-sd",
            params.get("subjects_directory")
        ])
    if params.get("umask") is not None:
        cargs.extend([
            "-umask",
            params.get("umask")
        ])
    if params.get("group_id") is not None:
        cargs.extend([
            "-grp",
            params.get("group_id")
        ])
    if params.get("allow_core_dump"):
        cargs.append("-allowcoredump")
    if params.get("debug_mode"):
        cargs.append("-debug")
    if params.get("dont_run"):
        cargs.append("-dontrun")
    if params.get("only_versions"):
        cargs.append("-onlyversions")
    if params.get("version_info"):
        cargs.append("-version")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def trac_all_outputs(
    params: TracAllParameters,
    execution: Execution,
) -> TracAllOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TracAllOutputs(
        root=execution.output_file("."),
        default_log=execution.output_file("scripts/trac-all.log"),
        default_cmd=execution.output_file("scripts/trac-all.cmd"),
    )
    return ret


def trac_all_execute(
    params: TracAllParameters,
    execution: Execution,
) -> TracAllOutputs:
    """
    Reconstruct white-matter pathways using an atlas of the underlying anatomy.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TracAllOutputs`).
    """
    params = execution.params(params)
    cargs = trac_all_cargs(params, execution)
    ret = trac_all_outputs(params, execution)
    execution.run(cargs)
    return ret


def trac_all(
    config_file: InputPathType | None = None,
    subject_name: str | None = None,
    dicom_file: InputPathType | None = None,
    pre_processing: bool = False,
    bedpost: bool = False,
    pathway_reconstruction: bool = False,
    assemble_measures: bool = False,
    image_corrections: bool = False,
    no_image_corrections: bool = False,
    image_quality_assessment: bool = False,
    no_image_quality_assessment: bool = False,
    intra_registration: bool = False,
    no_intra_registration: bool = False,
    tensor_fit: bool = False,
    no_tensor_fit: bool = False,
    inter_registration: bool = False,
    no_inter_registration: bool = False,
    pathway_priors: bool = False,
    no_pathway_priors: bool = False,
    infant_options: bool = False,
    job_file: InputPathType | None = None,
    log_file: str | None = None,
    no_append_log: bool = False,
    cmd_file: str | None = None,
    no_is_running: bool = False,
    subjects_directory: str | None = None,
    umask: str | None = None,
    group_id: str | None = None,
    allow_core_dump: bool = False,
    debug_mode: bool = False,
    dont_run: bool = False,
    only_versions: bool = False,
    version_info: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> TracAllOutputs:
    """
    Reconstruct white-matter pathways using an atlas of the underlying anatomy.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        config_file: Configuration file to set analysis options (dmrirc file).
        subject_name: Subject name (if not defined in dmrirc).
        dicom_file: Input DWI DICOM (if not defined in dmrirc).
        pre_processing: Perform pre-processing (step 1, all substeps).
        bedpost: Perform bedpost (step 2).
        pathway_reconstruction: Perform pathway reconstruction (step 3).
        assemble_measures: Assemble pathway measures from multiple subjects\
            (step 4).
        image_corrections: Perform image corrections (step 1.1).
        no_image_corrections: Skip image corrections (step 1.1).
        image_quality_assessment: Perform image quality assessment (step 1.2).
        no_image_quality_assessment: Skip image quality assessment (step 1.2).
        intra_registration: Perform intra-subject registration (step 1.3).
        no_intra_registration: Skip intra-subject registration (step 1.3).
        tensor_fit: Perform tensor fit (step 1.4).
        no_tensor_fit: Skip tensor fit (step 1.4).
        inter_registration: Perform inter-subject registration (step 1.5).
        no_inter_registration: Skip inter-subject registration (step 1.5).
        pathway_priors: Perform pathway priors (step 1.6).
        no_pathway_priors: Skip pathway priors (step 1.6).
        infant_options: Use infant brain processing options.
        job_file: Write a text file with command lines that can be run in\
            parallel and do not run them.
        log_file: Unique log file instead of the default scripts/trac-all.log.
        no_append_log: Overwrite old log files instead of appending.
        cmd_file: Unique cmd file instead of the default scripts/trac-all.cmd.
        no_is_running: Do not check whether subjects are currently being\
            processed.
        subjects_directory: Specify subjects directory (default environment\
            SUBJECTS_DIR).
        umask: Set Unix file permission mask (default 002).
        group_id: Check that current group is alpha groupid.
        allow_core_dump: Set coredump limit to unlimited.
        debug_mode: Generate much more output.
        dont_run: Do everything but execute each command.
        only_versions: Print version of each binary and exit.
        version_info: Print version of this script and exit.
        help_: Print full contents of help.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TracAllOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TRAC_ALL_METADATA)
    params = trac_all_params(
        config_file=config_file,
        subject_name=subject_name,
        dicom_file=dicom_file,
        pre_processing=pre_processing,
        bedpost=bedpost,
        pathway_reconstruction=pathway_reconstruction,
        assemble_measures=assemble_measures,
        image_corrections=image_corrections,
        no_image_corrections=no_image_corrections,
        image_quality_assessment=image_quality_assessment,
        no_image_quality_assessment=no_image_quality_assessment,
        intra_registration=intra_registration,
        no_intra_registration=no_intra_registration,
        tensor_fit=tensor_fit,
        no_tensor_fit=no_tensor_fit,
        inter_registration=inter_registration,
        no_inter_registration=no_inter_registration,
        pathway_priors=pathway_priors,
        no_pathway_priors=no_pathway_priors,
        infant_options=infant_options,
        job_file=job_file,
        log_file=log_file,
        no_append_log=no_append_log,
        cmd_file=cmd_file,
        no_is_running=no_is_running,
        subjects_directory=subjects_directory,
        umask=umask,
        group_id=group_id,
        allow_core_dump=allow_core_dump,
        debug_mode=debug_mode,
        dont_run=dont_run,
        only_versions=only_versions,
        version_info=version_info,
        help_=help_,
    )
    return trac_all_execute(params, execution)


__all__ = [
    "TRAC_ALL_METADATA",
    "TracAllOutputs",
    "TracAllParameters",
    "trac_all",
    "trac_all_params",
]
