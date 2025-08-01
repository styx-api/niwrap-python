# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

JKGCATRAIN_METADATA = Metadata(
    id="f73394990345946d6f0f0547594b7d0a8c67904f.boutiques",
    name="jkgcatrain",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


JkgcatrainParameters = typing.TypedDict('JkgcatrainParameters', {
    "__STYXTYPE__": typing.Literal["jkgcatrain"],
    "gca_directory": str,
    "iteration_number": typing.NotRequired[float | None],
    "num_threads": typing.NotRequired[float | None],
    "no_submit": bool,
    "mail_flag": bool,
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
        "jkgcatrain": jkgcatrain_cargs,
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


class JkgcatrainOutputs(typing.NamedTuple):
    """
    Output object returned when calling `jkgcatrain(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def jkgcatrain_params(
    gca_directory: str,
    iteration_number: float | None = 2,
    num_threads: float | None = None,
    no_submit: bool = False,
    mail_flag: bool = False,
) -> JkgcatrainParameters:
    """
    Build parameters.
    
    Args:
        gca_directory: Output directory from gcatrain.
        iteration_number: Iteration number (usually 2).
        num_threads: Number of threads to use.
        no_submit: Run serially, do not use pbsubmit.
        mail_flag: Mail to user when jobs are pbsubmitted or finished.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "jkgcatrain",
        "gca_directory": gca_directory,
        "no_submit": no_submit,
        "mail_flag": mail_flag,
    }
    if iteration_number is not None:
        params["iteration_number"] = iteration_number
    if num_threads is not None:
        params["num_threads"] = num_threads
    return params


def jkgcatrain_cargs(
    params: JkgcatrainParameters,
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
    cargs.append("jkgcatrain")
    cargs.extend([
        "--g",
        params.get("gca_directory")
    ])
    if params.get("iteration_number") is not None:
        cargs.extend([
            "--iter",
            str(params.get("iteration_number"))
        ])
    if params.get("num_threads") is not None:
        cargs.extend([
            "--nthreads",
            str(params.get("num_threads"))
        ])
    if params.get("no_submit"):
        cargs.append("--no-submit")
    if params.get("mail_flag"):
        cargs.append("--pb-m")
    return cargs


def jkgcatrain_outputs(
    params: JkgcatrainParameters,
    execution: Execution,
) -> JkgcatrainOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = JkgcatrainOutputs(
        root=execution.output_file("."),
    )
    return ret


def jkgcatrain_execute(
    params: JkgcatrainParameters,
    execution: Execution,
) -> JkgcatrainOutputs:
    """
    Jackknife training of GCA using existing output from gcatrain.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `JkgcatrainOutputs`).
    """
    params = execution.params(params)
    cargs = jkgcatrain_cargs(params, execution)
    ret = jkgcatrain_outputs(params, execution)
    execution.run(cargs)
    return ret


def jkgcatrain(
    gca_directory: str,
    iteration_number: float | None = 2,
    num_threads: float | None = None,
    no_submit: bool = False,
    mail_flag: bool = False,
    runner: Runner | None = None,
) -> JkgcatrainOutputs:
    """
    Jackknife training of GCA using existing output from gcatrain.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        gca_directory: Output directory from gcatrain.
        iteration_number: Iteration number (usually 2).
        num_threads: Number of threads to use.
        no_submit: Run serially, do not use pbsubmit.
        mail_flag: Mail to user when jobs are pbsubmitted or finished.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `JkgcatrainOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(JKGCATRAIN_METADATA)
    params = jkgcatrain_params(
        gca_directory=gca_directory,
        iteration_number=iteration_number,
        num_threads=num_threads,
        no_submit=no_submit,
        mail_flag=mail_flag,
    )
    return jkgcatrain_execute(params, execution)


__all__ = [
    "JKGCATRAIN_METADATA",
    "JkgcatrainOutputs",
    "JkgcatrainParameters",
    "jkgcatrain",
    "jkgcatrain_params",
]
