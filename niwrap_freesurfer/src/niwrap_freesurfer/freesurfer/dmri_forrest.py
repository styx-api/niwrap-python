# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DMRI_FORREST_METADATA = Metadata(
    id="783d39ff3f4d8b9efc1b1df20b2f6005684a7a50.boutiques",
    name="dmri_forrest",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


DmriForrestParameters = typing.TypedDict('DmriForrestParameters', {
    "__STYXTYPE__": typing.Literal["dmri_forrest"],
    "test_dir": str,
    "train_file": InputPathType,
    "mask_file": InputPathType,
    "tract_files": list[InputPathType],
    "seg_file": typing.NotRequired[InputPathType | None],
    "diff_file": typing.NotRequired[InputPathType | None],
    "debug": bool,
    "checkopts": bool,
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
        "dmri_forrest": dmri_forrest_cargs,
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


class DmriForrestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_forrest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dmri_forrest_params(
    test_dir: str,
    train_file: InputPathType,
    mask_file: InputPathType,
    tract_files: list[InputPathType],
    seg_file: InputPathType | None = None,
    diff_file: InputPathType | None = None,
    debug: bool = False,
    checkopts: bool = False,
    help_: bool = False,
) -> DmriForrestParameters:
    """
    Build parameters.
    
    Args:
        test_dir: Directory containing the test subject data.
        train_file: File listing training subject directories, one per line.
        mask_file: Input brain mask volume name, relative to subject directory.
        tract_files: Input tract label volume(s), relative to subject directory.
        seg_file: Input aparc+aseg volume name, relative to subject directory.
        diff_file: Input diffusion orientation volume name, relative to subject\
            directory.
        debug: Turn on debugging mode.
        checkopts: Only check options and exit.
        help_: Display help information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_forrest",
        "test_dir": test_dir,
        "train_file": train_file,
        "mask_file": mask_file,
        "tract_files": tract_files,
        "debug": debug,
        "checkopts": checkopts,
        "help": help_,
    }
    if seg_file is not None:
        params["seg_file"] = seg_file
    if diff_file is not None:
        params["diff_file"] = diff_file
    return params


def dmri_forrest_cargs(
    params: DmriForrestParameters,
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
    cargs.append("dmri_forrest")
    cargs.extend([
        "--test",
        params.get("test_dir")
    ])
    cargs.extend([
        "--train",
        execution.input_file(params.get("train_file"))
    ])
    cargs.extend([
        "--mask",
        execution.input_file(params.get("mask_file"))
    ])
    cargs.extend([
        "--tract",
        *[execution.input_file(f) for f in params.get("tract_files")]
    ])
    if params.get("seg_file") is not None:
        cargs.extend([
            "--seg",
            execution.input_file(params.get("seg_file"))
        ])
    if params.get("diff_file") is not None:
        cargs.extend([
            "--diff",
            execution.input_file(params.get("diff_file"))
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("checkopts"):
        cargs.append("--checkopts")
    if params.get("help"):
        cargs.append("--help")
    return cargs


def dmri_forrest_outputs(
    params: DmriForrestParameters,
    execution: Execution,
) -> DmriForrestOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriForrestOutputs(
        root=execution.output_file("."),
    )
    return ret


def dmri_forrest_execute(
    params: DmriForrestParameters,
    execution: Execution,
) -> DmriForrestOutputs:
    """
    dmri_forrest is a tool for processing diffusion MRI data using a random
    forest-based method.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriForrestOutputs`).
    """
    params = execution.params(params)
    cargs = dmri_forrest_cargs(params, execution)
    ret = dmri_forrest_outputs(params, execution)
    execution.run(cargs)
    return ret


def dmri_forrest(
    test_dir: str,
    train_file: InputPathType,
    mask_file: InputPathType,
    tract_files: list[InputPathType],
    seg_file: InputPathType | None = None,
    diff_file: InputPathType | None = None,
    debug: bool = False,
    checkopts: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> DmriForrestOutputs:
    """
    dmri_forrest is a tool for processing diffusion MRI data using a random
    forest-based method.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        test_dir: Directory containing the test subject data.
        train_file: File listing training subject directories, one per line.
        mask_file: Input brain mask volume name, relative to subject directory.
        tract_files: Input tract label volume(s), relative to subject directory.
        seg_file: Input aparc+aseg volume name, relative to subject directory.
        diff_file: Input diffusion orientation volume name, relative to subject\
            directory.
        debug: Turn on debugging mode.
        checkopts: Only check options and exit.
        help_: Display help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriForrestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_FORREST_METADATA)
    params = dmri_forrest_params(
        test_dir=test_dir,
        train_file=train_file,
        mask_file=mask_file,
        tract_files=tract_files,
        seg_file=seg_file,
        diff_file=diff_file,
        debug=debug,
        checkopts=checkopts,
        help_=help_,
    )
    return dmri_forrest_execute(params, execution)


__all__ = [
    "DMRI_FORREST_METADATA",
    "DmriForrestOutputs",
    "DmriForrestParameters",
    "dmri_forrest",
    "dmri_forrest_params",
]
