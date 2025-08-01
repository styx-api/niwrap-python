# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

GCAPREPONE_METADATA = Metadata(
    id="fea37ea95fe10bc19c820f21259071fe7046f12d.boutiques",
    name="gcaprepone",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


GcapreponeParameters = typing.TypedDict('GcapreponeParameters', {
    "__STYXTYPE__": typing.Literal["gcaprepone"],
    "gcadir": str,
    "subject": str,
    "init_subject": bool,
    "source_subjects_dir": str,
    "done_file": str,
    "no_emreg": bool,
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
        "gcaprepone": gcaprepone_cargs,
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


class GcapreponeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gcaprepone(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def gcaprepone_params(
    gcadir: str,
    subject: str,
    source_subjects_dir: str,
    done_file: str,
    init_subject: bool = False,
    no_emreg: bool = False,
) -> GcapreponeParameters:
    """
    Build parameters.
    
    Args:
        gcadir: Directory to be the new SUBJECTS_DIR.
        subject: Subject for the process.
        source_subjects_dir: SUBJECTS_DIR for source data.
        done_file: File to indicate completion.
        init_subject: Flag indicating the initial subject.
        no_emreg: Flag to skip EM registration.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gcaprepone",
        "gcadir": gcadir,
        "subject": subject,
        "init_subject": init_subject,
        "source_subjects_dir": source_subjects_dir,
        "done_file": done_file,
        "no_emreg": no_emreg,
    }
    return params


def gcaprepone_cargs(
    params: GcapreponeParameters,
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
    cargs.append("gcaprepone")
    cargs.extend([
        "--o",
        params.get("gcadir")
    ])
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    if params.get("init_subject"):
        cargs.append("--init-subject")
    cargs.extend([
        "--sd",
        params.get("source_subjects_dir")
    ])
    cargs.extend([
        "--done",
        params.get("done_file")
    ])
    if params.get("no_emreg"):
        cargs.append("--no-emreg")
    return cargs


def gcaprepone_outputs(
    params: GcapreponeParameters,
    execution: Execution,
) -> GcapreponeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GcapreponeOutputs(
        root=execution.output_file("."),
    )
    return ret


def gcaprepone_execute(
    params: GcapreponeParameters,
    execution: Execution,
) -> GcapreponeOutputs:
    """
    Tool for preparing FreeSurfer subjects for use with group-wise template
    generation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GcapreponeOutputs`).
    """
    params = execution.params(params)
    cargs = gcaprepone_cargs(params, execution)
    ret = gcaprepone_outputs(params, execution)
    execution.run(cargs)
    return ret


def gcaprepone(
    gcadir: str,
    subject: str,
    source_subjects_dir: str,
    done_file: str,
    init_subject: bool = False,
    no_emreg: bool = False,
    runner: Runner | None = None,
) -> GcapreponeOutputs:
    """
    Tool for preparing FreeSurfer subjects for use with group-wise template
    generation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        gcadir: Directory to be the new SUBJECTS_DIR.
        subject: Subject for the process.
        source_subjects_dir: SUBJECTS_DIR for source data.
        done_file: File to indicate completion.
        init_subject: Flag indicating the initial subject.
        no_emreg: Flag to skip EM registration.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GcapreponeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GCAPREPONE_METADATA)
    params = gcaprepone_params(
        gcadir=gcadir,
        subject=subject,
        init_subject=init_subject,
        source_subjects_dir=source_subjects_dir,
        done_file=done_file,
        no_emreg=no_emreg,
    )
    return gcaprepone_execute(params, execution)


__all__ = [
    "GCAPREPONE_METADATA",
    "GcapreponeOutputs",
    "GcapreponeParameters",
    "gcaprepone",
    "gcaprepone_params",
]
