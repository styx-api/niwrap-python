# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSLVBM_2_TEMPLATE_METADATA = Metadata(
    id="3a5ca9d9ae3d0b495395b095f669fd7d5c78293b.boutiques",
    name="fslvbm_2_template",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


Fslvbm2TemplateParameters = typing.TypedDict('Fslvbm2TemplateParameters', {
    "__STYX_TYPE__": typing.Literal["fslvbm_2_template"],
    "arch": typing.NotRequired[str | None],
    "coprocessor": typing.NotRequired[str | None],
    "coprocessor_multi": typing.NotRequired[str | None],
    "coprocessor_class": typing.NotRequired[str | None],
    "coprocessor_toolkit": typing.NotRequired[str | None],
    "jobhold": typing.NotRequired[str | None],
    "array_hold": typing.NotRequired[str | None],
    "logdir": typing.NotRequired[str | None],
    "mailoptions": typing.NotRequired[str | None],
    "mailto": typing.NotRequired[str | None],
    "name": typing.NotRequired[str | None],
    "priority": typing.NotRequired[str | None],
    "queue": typing.NotRequired[str | None],
    "resource": typing.NotRequired[str | None],
    "delete_job": typing.NotRequired[str | None],
    "memory_gb": typing.NotRequired[float | None],
    "parallel_env": typing.NotRequired[str | None],
    "array_task": typing.NotRequired[str | None],
    "array_native": typing.NotRequired[str | None],
    "num_tasks": typing.NotRequired[float | None],
    "coprocessor_name": typing.NotRequired[str | None],
    "project": typing.NotRequired[str | None],
    "runtime_limit": typing.NotRequired[float | None],
    "job_file": typing.NotRequired[InputPathType | None],
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
        "fslvbm_2_template": fslvbm_2_template_cargs,
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


class Fslvbm2TemplateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslvbm_2_template(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslvbm_2_template_params(
    arch: str | None = None,
    coprocessor: str | None = None,
    coprocessor_multi: str | None = None,
    coprocessor_class: str | None = None,
    coprocessor_toolkit: str | None = None,
    jobhold: str | None = None,
    array_hold: str | None = None,
    logdir: str | None = None,
    mailoptions: str | None = None,
    mailto: str | None = None,
    name: str | None = None,
    priority: str | None = None,
    queue_: str | None = None,
    resource_: str | None = None,
    delete_job: str | None = None,
    memory_gb: float | None = None,
    parallel_env: str | None = None,
    array_task: str | None = None,
    array_native: str | None = None,
    num_tasks: float | None = None,
    coprocessor_name: str | None = None,
    project: str | None = None,
    runtime_limit: float | None = None,
    job_file: InputPathType | None = None,
) -> Fslvbm2TemplateParameters:
    """
    Build parameters.
    
    Args:
        arch: Specify architecture.
        coprocessor: Specify coprocessor type.
        coprocessor_multi: Specify multiple coprocessors.
        coprocessor_class: Specify coprocessor class.
        coprocessor_toolkit: Specify coprocessor toolkit.
        jobhold: Hold job until specified job ID is completed.
        array_hold: Hold array job until specified job ID is completed.
        logdir: Specify log directory.
        mailoptions: Specify mail options.
        mailto: Specify email address for notifications.
        name: Specify job name.
        priority: Specify job priority.
        queue_: Specify queue.
        resource_: Specify resources.
        delete_job: Delete specified job.
        memory_gb: Specify memory in GB.
        parallel_env: Specify parallel environment and threads.
        array_task: Specify array task.
        array_native: Specify array native task.
        num_tasks: Specify number of tasks.
        coprocessor_name: Specify coprocessor name.
        project: Specify project.
        runtime_limit: Specify runtime limit in minutes.
        job_file: Specify job script file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslvbm_2_template",
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
    if memory_gb is not None:
        params["memory_gb"] = memory_gb
    if parallel_env is not None:
        params["parallel_env"] = parallel_env
    if array_task is not None:
        params["array_task"] = array_task
    if array_native is not None:
        params["array_native"] = array_native
    if num_tasks is not None:
        params["num_tasks"] = num_tasks
    if coprocessor_name is not None:
        params["coprocessor_name"] = coprocessor_name
    if project is not None:
        params["project"] = project
    if runtime_limit is not None:
        params["runtime_limit"] = runtime_limit
    if job_file is not None:
        params["job_file"] = job_file
    return params


def fslvbm_2_template_cargs(
    params: Fslvbm2TemplateParameters,
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
    cargs.append("fslvbm_2_template")
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
            params.get("coprocessor_multi")
        ])
    if params.get("coprocessor_class") is not None:
        cargs.extend([
            "--coprocessor_class",
            params.get("coprocessor_class")
        ])
    if params.get("coprocessor_toolkit") is not None:
        cargs.extend([
            "--coprocessor_toolkit",
            params.get("coprocessor_toolkit")
        ])
    if params.get("jobhold") is not None:
        cargs.extend([
            "-j",
            params.get("jobhold")
        ])
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
    if params.get("memory_gb") is not None:
        cargs.extend([
            "-R",
            str(params.get("memory_gb"))
        ])
    if params.get("parallel_env") is not None:
        cargs.extend([
            "-s",
            params.get("parallel_env")
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
    if params.get("num_tasks") is not None:
        cargs.extend([
            "-x",
            str(params.get("num_tasks"))
        ])
    if params.get("coprocessor_name") is not None:
        cargs.extend([
            "--has_coprocessor",
            params.get("coprocessor_name")
        ])
    if params.get("project") is not None:
        cargs.extend([
            "--project",
            params.get("project")
        ])
    if params.get("runtime_limit") is not None:
        cargs.extend([
            "-T",
            str(params.get("runtime_limit"))
        ])
    if params.get("job_file") is not None:
        cargs.extend([
            "-z",
            execution.input_file(params.get("job_file"))
        ])
    return cargs


def fslvbm_2_template_outputs(
    params: Fslvbm2TemplateParameters,
    execution: Execution,
) -> Fslvbm2TemplateOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Fslvbm2TemplateOutputs(
        root=execution.output_file("."),
    )
    return ret


def fslvbm_2_template_execute(
    params: Fslvbm2TemplateParameters,
    execution: Execution,
) -> Fslvbm2TemplateOutputs:
    """
    FSL-VBM is a Voxel-Based Morphometry style analysis tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Fslvbm2TemplateOutputs`).
    """
    params = execution.params(params)
    cargs = fslvbm_2_template_cargs(params, execution)
    ret = fslvbm_2_template_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslvbm_2_template(
    arch: str | None = None,
    coprocessor: str | None = None,
    coprocessor_multi: str | None = None,
    coprocessor_class: str | None = None,
    coprocessor_toolkit: str | None = None,
    jobhold: str | None = None,
    array_hold: str | None = None,
    logdir: str | None = None,
    mailoptions: str | None = None,
    mailto: str | None = None,
    name: str | None = None,
    priority: str | None = None,
    queue_: str | None = None,
    resource_: str | None = None,
    delete_job: str | None = None,
    memory_gb: float | None = None,
    parallel_env: str | None = None,
    array_task: str | None = None,
    array_native: str | None = None,
    num_tasks: float | None = None,
    coprocessor_name: str | None = None,
    project: str | None = None,
    runtime_limit: float | None = None,
    job_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> Fslvbm2TemplateOutputs:
    """
    FSL-VBM is a Voxel-Based Morphometry style analysis tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        arch: Specify architecture.
        coprocessor: Specify coprocessor type.
        coprocessor_multi: Specify multiple coprocessors.
        coprocessor_class: Specify coprocessor class.
        coprocessor_toolkit: Specify coprocessor toolkit.
        jobhold: Hold job until specified job ID is completed.
        array_hold: Hold array job until specified job ID is completed.
        logdir: Specify log directory.
        mailoptions: Specify mail options.
        mailto: Specify email address for notifications.
        name: Specify job name.
        priority: Specify job priority.
        queue_: Specify queue.
        resource_: Specify resources.
        delete_job: Delete specified job.
        memory_gb: Specify memory in GB.
        parallel_env: Specify parallel environment and threads.
        array_task: Specify array task.
        array_native: Specify array native task.
        num_tasks: Specify number of tasks.
        coprocessor_name: Specify coprocessor name.
        project: Specify project.
        runtime_limit: Specify runtime limit in minutes.
        job_file: Specify job script file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Fslvbm2TemplateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLVBM_2_TEMPLATE_METADATA)
    params = fslvbm_2_template_params(
        arch=arch,
        coprocessor=coprocessor,
        coprocessor_multi=coprocessor_multi,
        coprocessor_class=coprocessor_class,
        coprocessor_toolkit=coprocessor_toolkit,
        jobhold=jobhold,
        array_hold=array_hold,
        logdir=logdir,
        mailoptions=mailoptions,
        mailto=mailto,
        name=name,
        priority=priority,
        queue_=queue_,
        resource_=resource_,
        delete_job=delete_job,
        memory_gb=memory_gb,
        parallel_env=parallel_env,
        array_task=array_task,
        array_native=array_native,
        num_tasks=num_tasks,
        coprocessor_name=coprocessor_name,
        project=project,
        runtime_limit=runtime_limit,
        job_file=job_file,
    )
    return fslvbm_2_template_execute(params, execution)


__all__ = [
    "FSLVBM_2_TEMPLATE_METADATA",
    "Fslvbm2TemplateOutputs",
    "Fslvbm2TemplateParameters",
    "fslvbm_2_template",
    "fslvbm_2_template_params",
]
