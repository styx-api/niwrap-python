# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FS_CHECK_VERSION_METADATA = Metadata(
    id="ac2742ad52c0ec9531a37b18769e9a1969669e97.boutiques",
    name="fs-check-version",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


FsCheckVersionParameters = typing.TypedDict('FsCheckVersionParameters', {
    "__STYXTYPE__": typing.Literal["fs-check-version"],
    "subjects_dir": str,
    "outfile": str,
    "subject": typing.NotRequired[str | None],
    "require_match": bool,
    "no_require_match": bool,
    "test": bool,
    "test_debug": bool,
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
        "fs-check-version": fs_check_version_cargs,
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
        "fs-check-version": fs_check_version_outputs,
    }.get(t)


class FsCheckVersionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fs_check_version(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output text file with a 1 if the version matches, otherwise 0"""


def fs_check_version_params(
    subjects_dir: str,
    outfile: str,
    subject: str | None = None,
    require_match: bool = False,
    no_require_match: bool = False,
    test: bool = False,
    test_debug: bool = False,
) -> FsCheckVersionParameters:
    """
    Build parameters.
    
    Args:
        subjects_dir: Subjects directory path.
        outfile: Output file path where result of version check will be written.
        subject: Subject name (optional).
        require_match: Set REQUIRE_FS_MATCH for testing.
        no_require_match: Unset REQUIRE_FS_MATCH for testing.
        test: Go through permutations for testing.
        test_debug: Go through permutations for debugging.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fs-check-version",
        "subjects_dir": subjects_dir,
        "outfile": outfile,
        "require_match": require_match,
        "no_require_match": no_require_match,
        "test": test,
        "test_debug": test_debug,
    }
    if subject is not None:
        params["subject"] = subject
    return params


def fs_check_version_cargs(
    params: FsCheckVersionParameters,
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
    cargs.append("fs-check-version")
    cargs.extend([
        "--sd",
        params.get("subjects_dir")
    ])
    cargs.extend([
        "--o",
        params.get("outfile")
    ])
    if params.get("subject") is not None:
        cargs.extend([
            "--s",
            params.get("subject")
        ])
    if params.get("require_match"):
        cargs.append("--require-match")
    if params.get("no_require_match"):
        cargs.append("--no-require-match")
    if params.get("test"):
        cargs.append("--test")
    if params.get("test_debug"):
        cargs.append("--test-debug")
    return cargs


def fs_check_version_outputs(
    params: FsCheckVersionParameters,
    execution: Execution,
) -> FsCheckVersionOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsCheckVersionOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("outfile")),
    )
    return ret


def fs_check_version_execute(
    params: FsCheckVersionParameters,
    execution: Execution,
) -> FsCheckVersionOutputs:
    """
    Script to manage which version of FreeSurfer can be used to analyze data
    ensuring consistency with the desired version.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsCheckVersionOutputs`).
    """
    params = execution.params(params)
    cargs = fs_check_version_cargs(params, execution)
    ret = fs_check_version_outputs(params, execution)
    execution.run(cargs)
    return ret


def fs_check_version(
    subjects_dir: str,
    outfile: str,
    subject: str | None = None,
    require_match: bool = False,
    no_require_match: bool = False,
    test: bool = False,
    test_debug: bool = False,
    runner: Runner | None = None,
) -> FsCheckVersionOutputs:
    """
    Script to manage which version of FreeSurfer can be used to analyze data
    ensuring consistency with the desired version.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects_dir: Subjects directory path.
        outfile: Output file path where result of version check will be written.
        subject: Subject name (optional).
        require_match: Set REQUIRE_FS_MATCH for testing.
        no_require_match: Unset REQUIRE_FS_MATCH for testing.
        test: Go through permutations for testing.
        test_debug: Go through permutations for debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsCheckVersionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FS_CHECK_VERSION_METADATA)
    params = fs_check_version_params(
        subjects_dir=subjects_dir,
        outfile=outfile,
        subject=subject,
        require_match=require_match,
        no_require_match=no_require_match,
        test=test,
        test_debug=test_debug,
    )
    return fs_check_version_execute(params, execution)


__all__ = [
    "FS_CHECK_VERSION_METADATA",
    "FsCheckVersionOutputs",
    "FsCheckVersionParameters",
    "fs_check_version",
    "fs_check_version_params",
]
