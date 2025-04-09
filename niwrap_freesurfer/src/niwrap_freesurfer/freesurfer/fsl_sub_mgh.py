# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_SUB_MGH_METADATA = Metadata(
    id="4015aeacaae283d33f0b4ca8406dbe45c4046304.boutiques",
    name="fsl_sub_mgh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


FslSubMghParameters = typing.TypedDict('FslSubMghParameters', {
    "__STYX_TYPE__": typing.Literal["fsl_sub_mgh"],
    "estimated_time": typing.NotRequired[int | None],
    "queue_name": typing.NotRequired[str | None],
    "architecture": typing.NotRequired[str | None],
    "job_priority": typing.NotRequired[int | None],
    "email_address": typing.NotRequired[str | None],
    "hold_job": typing.NotRequired[str | None],
    "task_file": typing.NotRequired[InputPathType | None],
    "job_name": typing.NotRequired[str | None],
    "log_dir": typing.NotRequired[str | None],
    "mail_options": typing.NotRequired[str | None],
    "flags_in_scripts": bool,
    "verbose": bool,
    "shell_path": typing.NotRequired[str | None],
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
        "fsl_sub_mgh": fsl_sub_mgh_cargs,
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


class FslSubMghOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_sub_mgh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsl_sub_mgh_params(
    estimated_time: int | None = None,
    queue_name: str | None = "long.q",
    architecture: str | None = None,
    job_priority: int | None = 0,
    email_address: str | None = "root@fmrib.ox.ac.uk",
    hold_job: str | None = None,
    task_file: InputPathType | None = None,
    job_name: str | None = None,
    log_dir: str | None = None,
    mail_options: str | None = None,
    flags_in_scripts: bool = False,
    verbose: bool = False,
    shell_path: str | None = None,
) -> FslSubMghParameters:
    """
    Build parameters.
    
    Args:
        estimated_time: Estimated job length in minutes, used to auto-set queue\
            name.
        queue_name: Queue name. Possible values are 'verylong.q', 'long.q' and\
            'short.q'. Default is 'long.q'.
        architecture: Architecture [e.g., darwin or lx24-amd64].
        job_priority: Job priority [0:-1024]. Default is 0.
        email_address: Email address to send notifications. Default is\
            root@fmrib.ox.ac.uk.
        hold_job: Job ID to place a hold on this task until completion.
        task_file: Task file of commands to execute in parallel.
        job_name: Specify job name as it will appear on the queue.
        log_dir: Output directory for log files.
        mail_options: Change the SGE mail options.
        flags_in_scripts: Use flags embedded in scripts to set SGE queuing\
            options.
        verbose: Verbose mode.
        shell_path: Change the PBS shell option.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_sub_mgh",
        "flags_in_scripts": flags_in_scripts,
        "verbose": verbose,
    }
    if estimated_time is not None:
        params["estimated_time"] = estimated_time
    if queue_name is not None:
        params["queue_name"] = queue_name
    if architecture is not None:
        params["architecture"] = architecture
    if job_priority is not None:
        params["job_priority"] = job_priority
    if email_address is not None:
        params["email_address"] = email_address
    if hold_job is not None:
        params["hold_job"] = hold_job
    if task_file is not None:
        params["task_file"] = task_file
    if job_name is not None:
        params["job_name"] = job_name
    if log_dir is not None:
        params["log_dir"] = log_dir
    if mail_options is not None:
        params["mail_options"] = mail_options
    if shell_path is not None:
        params["shell_path"] = shell_path
    return params


def fsl_sub_mgh_cargs(
    params: FslSubMghParameters,
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
    cargs.append("fsl_sub_mgh")
    if params.get("estimated_time") is not None:
        cargs.extend([
            "-T",
            str(params.get("estimated_time"))
        ])
    if params.get("queue_name") is not None:
        cargs.extend([
            "-q",
            params.get("queue_name")
        ])
    if params.get("architecture") is not None:
        cargs.extend([
            "-a",
            params.get("architecture")
        ])
    if params.get("job_priority") is not None:
        cargs.extend([
            "-p",
            str(params.get("job_priority"))
        ])
    if params.get("email_address") is not None:
        cargs.extend([
            "-M",
            params.get("email_address")
        ])
    if params.get("hold_job") is not None:
        cargs.extend([
            "-j",
            params.get("hold_job")
        ])
    if params.get("task_file") is not None:
        cargs.extend([
            "-t",
            execution.input_file(params.get("task_file"))
        ])
    if params.get("job_name") is not None:
        cargs.extend([
            "-N",
            params.get("job_name")
        ])
    if params.get("log_dir") is not None:
        cargs.extend([
            "-l",
            params.get("log_dir")
        ])
    if params.get("mail_options") is not None:
        cargs.extend([
            "-m",
            params.get("mail_options")
        ])
    if params.get("flags_in_scripts"):
        cargs.append("-F")
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("shell_path") is not None:
        cargs.extend([
            "-s",
            params.get("shell_path")
        ])
    return cargs


def fsl_sub_mgh_outputs(
    params: FslSubMghParameters,
    execution: Execution,
) -> FslSubMghOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslSubMghOutputs(
        root=execution.output_file("."),
    )
    return ret


def fsl_sub_mgh_execute(
    params: FslSubMghParameters,
    execution: Execution,
) -> FslSubMghOutputs:
    """
    Wrapper for job control system such as SGE, modified for compatibility with the
    PBS queueing system.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslSubMghOutputs`).
    """
    params = execution.params(params)
    cargs = fsl_sub_mgh_cargs(params, execution)
    ret = fsl_sub_mgh_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_sub_mgh(
    estimated_time: int | None = None,
    queue_name: str | None = "long.q",
    architecture: str | None = None,
    job_priority: int | None = 0,
    email_address: str | None = "root@fmrib.ox.ac.uk",
    hold_job: str | None = None,
    task_file: InputPathType | None = None,
    job_name: str | None = None,
    log_dir: str | None = None,
    mail_options: str | None = None,
    flags_in_scripts: bool = False,
    verbose: bool = False,
    shell_path: str | None = None,
    runner: Runner | None = None,
) -> FslSubMghOutputs:
    """
    Wrapper for job control system such as SGE, modified for compatibility with the
    PBS queueing system.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        estimated_time: Estimated job length in minutes, used to auto-set queue\
            name.
        queue_name: Queue name. Possible values are 'verylong.q', 'long.q' and\
            'short.q'. Default is 'long.q'.
        architecture: Architecture [e.g., darwin or lx24-amd64].
        job_priority: Job priority [0:-1024]. Default is 0.
        email_address: Email address to send notifications. Default is\
            root@fmrib.ox.ac.uk.
        hold_job: Job ID to place a hold on this task until completion.
        task_file: Task file of commands to execute in parallel.
        job_name: Specify job name as it will appear on the queue.
        log_dir: Output directory for log files.
        mail_options: Change the SGE mail options.
        flags_in_scripts: Use flags embedded in scripts to set SGE queuing\
            options.
        verbose: Verbose mode.
        shell_path: Change the PBS shell option.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslSubMghOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_SUB_MGH_METADATA)
    params = fsl_sub_mgh_params(
        estimated_time=estimated_time,
        queue_name=queue_name,
        architecture=architecture,
        job_priority=job_priority,
        email_address=email_address,
        hold_job=hold_job,
        task_file=task_file,
        job_name=job_name,
        log_dir=log_dir,
        mail_options=mail_options,
        flags_in_scripts=flags_in_scripts,
        verbose=verbose,
        shell_path=shell_path,
    )
    return fsl_sub_mgh_execute(params, execution)


__all__ = [
    "FSL_SUB_MGH_METADATA",
    "FslSubMghOutputs",
    "FslSubMghParameters",
    "fsl_sub_mgh",
    "fsl_sub_mgh_params",
]
