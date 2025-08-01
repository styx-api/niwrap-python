# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSL_SUB_METADATA = Metadata(
    id="027e69ca7c58056d4c9c91424022f6d56c591d77.boutiques",
    name="fsl_sub",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


FslSubParameters = typing.TypedDict('FslSubParameters', {
    "__STYXTYPE__": typing.Literal["fsl_sub"],
    "arch": typing.NotRequired[str | None],
    "coprocessor": typing.NotRequired[str | None],
    "coprocessor_multi": typing.NotRequired[float | None],
    "coprocessor_class": typing.NotRequired[str | None],
    "coprocessor_class_strict": bool,
    "coprocessor_toolkit": typing.NotRequired[str | None],
    "usescript": bool,
    "jobhold": typing.NotRequired[str | None],
    "not_requeueable": bool,
    "array_hold": typing.NotRequired[str | None],
    "logdir": typing.NotRequired[str | None],
    "mailoptions": typing.NotRequired[str | None],
    "mailto": typing.NotRequired[str | None],
    "novalidation": bool,
    "name": typing.NotRequired[str | None],
    "priority": typing.NotRequired[str | None],
    "queue": typing.NotRequired[str | None],
    "resource": typing.NotRequired[str | None],
    "delete_job": typing.NotRequired[str | None],
    "jobram": typing.NotRequired[float | None],
    "parallelenv_threads": typing.NotRequired[str | None],
    "array_task": typing.NotRequired[str | None],
    "array_native": typing.NotRequired[str | None],
    "array_limit": typing.NotRequired[float | None],
    "keep_jobscript": bool,
    "project": typing.NotRequired[str | None],
    "noramsplit": bool,
    "jobtime": typing.NotRequired[float | None],
    "has_coprocessor": typing.NotRequired[str | None],
    "has_queues": bool,
    "show_config": bool,
    "verbose": bool,
    "version": bool,
    "fileisimage": typing.NotRequired[InputPathType | None],
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
        "fsl_sub": fsl_sub_cargs,
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


class FslSubOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_sub(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsl_sub_params(
    arch: str | None = None,
    coprocessor: str | None = None,
    coprocessor_multi: float | None = None,
    coprocessor_class: str | None = None,
    coprocessor_class_strict: bool = False,
    coprocessor_toolkit: str | None = None,
    usescript: bool = False,
    jobhold: str | None = None,
    not_requeueable: bool = False,
    array_hold: str | None = None,
    logdir: str | None = None,
    mailoptions: str | None = None,
    mailto: str | None = "root@fe8ea96c3a1a",
    novalidation: bool = False,
    name: str | None = None,
    priority: str | None = None,
    queue_: str | None = None,
    resource_: str | None = None,
    delete_job: str | None = None,
    jobram: float | None = None,
    parallelenv_threads: str | None = None,
    array_task: str | None = None,
    array_native: str | None = None,
    array_limit: float | None = None,
    keep_jobscript: bool = False,
    project: str | None = None,
    noramsplit: bool = False,
    jobtime: float | None = None,
    has_coprocessor: str | None = None,
    has_queues: bool = False,
    show_config: bool = False,
    verbose: bool = False,
    version: bool = False,
    fileisimage: InputPathType | None = None,
) -> FslSubParameters:
    """
    Build parameters.
    
    Args:
        arch: Architectures not available.
        coprocessor: No co-processor configured - ignored.
        coprocessor_multi: No co-processor configured - ignored.
        coprocessor_class: No co-processor classes configured - ignored.
        coprocessor_class_strict: No co-processor classes configured - ignored.
        coprocessor_toolkit: No co-processor toolkits configured - ignored.
        usescript: Use flags embedded in scripts to set queuing options - not\
            supported.
        jobhold: Place a hold on this task until specified job id has\
            completed.
        not_requeueable: Job cannot be requeued in the event of a node failure.
        array_hold: Not supported - will be converted to simple job hold.
        logdir: Where to output logfiles.
        mailoptions: Email notification options (ignored).
        mailto: Email notification recipients (ignored).
        novalidation: Don't check for presence of script/binary in your\
            searchpath.
        name: Specify job name as it will appear on queue.
        priority: Specify job priority (not supported).
        queue_: Specify the queue for the job (irrelevant if not running in a\
            cluster environment).
        resource_: Pass a resource request or constraint string through to the\
            job scheduler.
        delete_job: Deletes a queued/running job.
        jobram: Max total RAM required for job (integer in GB).
        parallelenv_threads: No parallel environments configured.
        array_task: Specify a task file of commands to execute in parallel.
        array_native: Binary/Script will handle array task internally (mutually\
            exclusive with --array_task).
        array_limit: Specify the maximum number of parallel job sub-tasks to\
            run concurrently.
        keep_jobscript: Whether to create and save a job submission script.
        project: Specify the project (not relevant when not running in a\
            cluster environment).
        noramsplit: Disable RAM splitting (not relevant when not running in a\
            cluster environment).
        jobtime: Estimated job length in minutes, used to automatically choose\
            the queue name.
        has_coprocessor: fsl_sub returns with exit code of 0 if specified\
            coprocessor is configured.
        has_queues: fsl_sub returns with exit code of 0 if there's a compute\
            cluster with queues configured.
        show_config: Display the configuration currently in force.
        verbose: Verbose mode.
        version: Show program's version number and exit.
        fileisimage: If <file> already exists and is an MRI image file, do\
            nothing and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsl_sub",
        "coprocessor_class_strict": coprocessor_class_strict,
        "usescript": usescript,
        "not_requeueable": not_requeueable,
        "novalidation": novalidation,
        "keep_jobscript": keep_jobscript,
        "noramsplit": noramsplit,
        "has_queues": has_queues,
        "show_config": show_config,
        "verbose": verbose,
        "version": version,
    }
    if arch is not None:
        params["arch"] = arch
    if coprocessor is not None:
        params["coprocessor"] = coprocessor
    if coprocessor_multi is not None:
        params["coprocessor_multi"] = coprocessor_multi
    if coprocessor_class is not None:
        params["coprocessor_class"] = coprocessor_class
    if coprocessor_toolkit is not None:
        params["coprocessor_toolkit"] = coprocessor_toolkit
    if jobhold is not None:
        params["jobhold"] = jobhold
    if array_hold is not None:
        params["array_hold"] = array_hold
    if logdir is not None:
        params["logdir"] = logdir
    if mailoptions is not None:
        params["mailoptions"] = mailoptions
    if mailto is not None:
        params["mailto"] = mailto
    if name is not None:
        params["name"] = name
    if priority is not None:
        params["priority"] = priority
    if queue_ is not None:
        params["queue"] = queue_
    if resource_ is not None:
        params["resource"] = resource_
    if delete_job is not None:
        params["delete_job"] = delete_job
    if jobram is not None:
        params["jobram"] = jobram
    if parallelenv_threads is not None:
        params["parallelenv_threads"] = parallelenv_threads
    if array_task is not None:
        params["array_task"] = array_task
    if array_native is not None:
        params["array_native"] = array_native
    if array_limit is not None:
        params["array_limit"] = array_limit
    if project is not None:
        params["project"] = project
    if jobtime is not None:
        params["jobtime"] = jobtime
    if has_coprocessor is not None:
        params["has_coprocessor"] = has_coprocessor
    if fileisimage is not None:
        params["fileisimage"] = fileisimage
    return params


def fsl_sub_cargs(
    params: FslSubParameters,
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
    cargs.append("fsl_sub")
    if params.get("arch") is not None:
        cargs.extend([
            "-a",
            params.get("arch")
        ])
    if params.get("coprocessor") is not None:
        cargs.extend([
            "-c",
            params.get("coprocessor")
        ])
    if params.get("coprocessor_multi") is not None:
        cargs.extend([
            "--coprocessor_multi",
            str(params.get("coprocessor_multi"))
        ])
    if params.get("coprocessor_class") is not None:
        cargs.extend([
            "--coprocessor_class",
            params.get("coprocessor_class")
        ])
    if params.get("coprocessor_class_strict"):
        cargs.append("--coprocessor_class_strict")
    if params.get("coprocessor_toolkit") is not None:
        cargs.extend([
            "--coprocessor_toolkit",
            params.get("coprocessor_toolkit")
        ])
    if params.get("usescript"):
        cargs.append("-F")
    if params.get("jobhold") is not None:
        cargs.extend([
            "-j",
            params.get("jobhold")
        ])
    if params.get("not_requeueable"):
        cargs.append("--not_requeueable")
    if params.get("array_hold") is not None:
        cargs.extend([
            "--array_hold",
            params.get("array_hold")
        ])
    if params.get("logdir") is not None:
        cargs.extend([
            "-l",
            params.get("logdir")
        ])
    if params.get("mailoptions") is not None:
        cargs.extend([
            "-m",
            params.get("mailoptions")
        ])
    if params.get("mailto") is not None:
        cargs.extend([
            "-M",
            params.get("mailto")
        ])
    if params.get("novalidation"):
        cargs.append("-n")
    if params.get("name") is not None:
        cargs.extend([
            "-N",
            params.get("name")
        ])
    if params.get("priority") is not None:
        cargs.extend([
            "-p",
            params.get("priority")
        ])
    if params.get("queue") is not None:
        cargs.extend([
            "-q",
            params.get("queue")
        ])
    if params.get("resource") is not None:
        cargs.extend([
            "-r",
            params.get("resource")
        ])
    if params.get("delete_job") is not None:
        cargs.extend([
            "--delete_job",
            params.get("delete_job")
        ])
    if params.get("jobram") is not None:
        cargs.extend([
            "-R",
            str(params.get("jobram"))
        ])
    if params.get("parallelenv_threads") is not None:
        cargs.extend([
            "-s",
            params.get("parallelenv_threads")
        ])
    if params.get("array_task") is not None:
        cargs.extend([
            "-t",
            params.get("array_task")
        ])
    if params.get("array_native") is not None:
        cargs.extend([
            "--array_native",
            params.get("array_native")
        ])
    if params.get("array_limit") is not None:
        cargs.extend([
            "-x",
            str(params.get("array_limit"))
        ])
    if params.get("keep_jobscript"):
        cargs.append("--keep_jobscript")
    if params.get("project") is not None:
        cargs.extend([
            "--project",
            params.get("project")
        ])
    if params.get("noramsplit"):
        cargs.append("-S")
    if params.get("jobtime") is not None:
        cargs.extend([
            "-T",
            str(params.get("jobtime"))
        ])
    if params.get("has_coprocessor") is not None:
        cargs.extend([
            "--has_coprocessor",
            params.get("has_coprocessor")
        ])
    if params.get("has_queues"):
        cargs.append("--has_queues")
    if params.get("show_config"):
        cargs.append("--show_config")
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("version"):
        cargs.append("-V")
    if params.get("fileisimage") is not None:
        cargs.extend([
            "-z",
            execution.input_file(params.get("fileisimage"))
        ])
    return cargs


def fsl_sub_outputs(
    params: FslSubParameters,
    execution: Execution,
) -> FslSubOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FslSubOutputs(
        root=execution.output_file("."),
    )
    return ret


def fsl_sub_execute(
    params: FslSubParameters,
    execution: Execution,
) -> FslSubOutputs:
    """
    FSL cluster submission tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FslSubOutputs`).
    """
    params = execution.params(params)
    cargs = fsl_sub_cargs(params, execution)
    ret = fsl_sub_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsl_sub(
    arch: str | None = None,
    coprocessor: str | None = None,
    coprocessor_multi: float | None = None,
    coprocessor_class: str | None = None,
    coprocessor_class_strict: bool = False,
    coprocessor_toolkit: str | None = None,
    usescript: bool = False,
    jobhold: str | None = None,
    not_requeueable: bool = False,
    array_hold: str | None = None,
    logdir: str | None = None,
    mailoptions: str | None = None,
    mailto: str | None = "root@fe8ea96c3a1a",
    novalidation: bool = False,
    name: str | None = None,
    priority: str | None = None,
    queue_: str | None = None,
    resource_: str | None = None,
    delete_job: str | None = None,
    jobram: float | None = None,
    parallelenv_threads: str | None = None,
    array_task: str | None = None,
    array_native: str | None = None,
    array_limit: float | None = None,
    keep_jobscript: bool = False,
    project: str | None = None,
    noramsplit: bool = False,
    jobtime: float | None = None,
    has_coprocessor: str | None = None,
    has_queues: bool = False,
    show_config: bool = False,
    verbose: bool = False,
    version: bool = False,
    fileisimage: InputPathType | None = None,
    runner: Runner | None = None,
) -> FslSubOutputs:
    """
    FSL cluster submission tool.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        arch: Architectures not available.
        coprocessor: No co-processor configured - ignored.
        coprocessor_multi: No co-processor configured - ignored.
        coprocessor_class: No co-processor classes configured - ignored.
        coprocessor_class_strict: No co-processor classes configured - ignored.
        coprocessor_toolkit: No co-processor toolkits configured - ignored.
        usescript: Use flags embedded in scripts to set queuing options - not\
            supported.
        jobhold: Place a hold on this task until specified job id has\
            completed.
        not_requeueable: Job cannot be requeued in the event of a node failure.
        array_hold: Not supported - will be converted to simple job hold.
        logdir: Where to output logfiles.
        mailoptions: Email notification options (ignored).
        mailto: Email notification recipients (ignored).
        novalidation: Don't check for presence of script/binary in your\
            searchpath.
        name: Specify job name as it will appear on queue.
        priority: Specify job priority (not supported).
        queue_: Specify the queue for the job (irrelevant if not running in a\
            cluster environment).
        resource_: Pass a resource request or constraint string through to the\
            job scheduler.
        delete_job: Deletes a queued/running job.
        jobram: Max total RAM required for job (integer in GB).
        parallelenv_threads: No parallel environments configured.
        array_task: Specify a task file of commands to execute in parallel.
        array_native: Binary/Script will handle array task internally (mutually\
            exclusive with --array_task).
        array_limit: Specify the maximum number of parallel job sub-tasks to\
            run concurrently.
        keep_jobscript: Whether to create and save a job submission script.
        project: Specify the project (not relevant when not running in a\
            cluster environment).
        noramsplit: Disable RAM splitting (not relevant when not running in a\
            cluster environment).
        jobtime: Estimated job length in minutes, used to automatically choose\
            the queue name.
        has_coprocessor: fsl_sub returns with exit code of 0 if specified\
            coprocessor is configured.
        has_queues: fsl_sub returns with exit code of 0 if there's a compute\
            cluster with queues configured.
        show_config: Display the configuration currently in force.
        verbose: Verbose mode.
        version: Show program's version number and exit.
        fileisimage: If <file> already exists and is an MRI image file, do\
            nothing and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslSubOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_SUB_METADATA)
    params = fsl_sub_params(
        arch=arch,
        coprocessor=coprocessor,
        coprocessor_multi=coprocessor_multi,
        coprocessor_class=coprocessor_class,
        coprocessor_class_strict=coprocessor_class_strict,
        coprocessor_toolkit=coprocessor_toolkit,
        usescript=usescript,
        jobhold=jobhold,
        not_requeueable=not_requeueable,
        array_hold=array_hold,
        logdir=logdir,
        mailoptions=mailoptions,
        mailto=mailto,
        novalidation=novalidation,
        name=name,
        priority=priority,
        queue_=queue_,
        resource_=resource_,
        delete_job=delete_job,
        jobram=jobram,
        parallelenv_threads=parallelenv_threads,
        array_task=array_task,
        array_native=array_native,
        array_limit=array_limit,
        keep_jobscript=keep_jobscript,
        project=project,
        noramsplit=noramsplit,
        jobtime=jobtime,
        has_coprocessor=has_coprocessor,
        has_queues=has_queues,
        show_config=show_config,
        verbose=verbose,
        version=version,
        fileisimage=fileisimage,
    )
    return fsl_sub_execute(params, execution)


__all__ = [
    "FSL_SUB_METADATA",
    "FslSubOutputs",
    "FslSubParameters",
    "fsl_sub",
    "fsl_sub_params",
]
