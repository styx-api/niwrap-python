# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__RENAME_PANGA_METADATA = Metadata(
    id="667fb48aeb92a9756a0ac4f7c1ba77ceb5554bab.boutiques",
    name="@RenamePanga",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VRenamePangaParameters = typing.TypedDict('VRenamePangaParameters', {
    "__STYXTYPE__": typing.Literal["@RenamePanga"],
    "dir_number": str,
    "first_image_number": str,
    "num_slices": float,
    "num_reps": float,
    "output_root": str,
    "keep_prefix": bool,
    "interactive": bool,
    "outliers_check": bool,
    "slice_pattern": typing.NotRequired[str | None],
    "output_directory": typing.NotRequired[str | None],
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
        "@RenamePanga": v__rename_panga_cargs,
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
        "@RenamePanga": v__rename_panga_outputs,
    }.get(t)


class VRenamePangaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__rename_panga(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    head_file: OutputPathType | None
    """Main output file (HEAD)"""
    brik_file: OutputPathType | None
    """Main output file (BRIK)"""
    log_file: OutputPathType | None
    """Log file created in the current directory"""


def v__rename_panga_params(
    dir_number: str,
    first_image_number: str,
    num_slices: float,
    num_reps: float,
    output_root: str,
    keep_prefix: bool = False,
    interactive: bool = False,
    outliers_check: bool = False,
    slice_pattern: str | None = None,
    output_directory: str | None = None,
) -> VRenamePangaParameters:
    """
    Build parameters.
    
    Args:
        dir_number: The directory number where the first image of the series is\
            stored.
        first_image_number: The number of the first image in the series.
        num_slices: The number of slices making up the imaged volume.
        num_reps: The number of samples in your time series.
        output_root: The prefix for the output brick.
        keep_prefix: Forces @RenamePanga to use the prefix you designate\
            without modification.
        interactive: Launches to3d in interactive mode. This allows you to\
            double check the automated settings.
        outliers_check: Performs outliers check and writes the outliers to a\
            .1D file placed in the output directory.
        slice_pattern: Sets the slice acquisition pattern. The default option\
            is alt+z.
        output_directory: Directory where the output (bricks and 1D files) will\
            be stored. The default directory is ./afni.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@RenamePanga",
        "dir_number": dir_number,
        "first_image_number": first_image_number,
        "num_slices": num_slices,
        "num_reps": num_reps,
        "output_root": output_root,
        "keep_prefix": keep_prefix,
        "interactive": interactive,
        "outliers_check": outliers_check,
    }
    if slice_pattern is not None:
        params["slice_pattern"] = slice_pattern
    if output_directory is not None:
        params["output_directory"] = output_directory
    return params


def v__rename_panga_cargs(
    params: VRenamePangaParameters,
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
    cargs.append("@RenamePanga")
    cargs.append(params.get("dir_number"))
    cargs.append(params.get("first_image_number"))
    cargs.append(str(params.get("num_slices")))
    cargs.append(str(params.get("num_reps")))
    cargs.append(params.get("output_root"))
    if params.get("keep_prefix"):
        cargs.append("-kp")
    if params.get("interactive"):
        cargs.append("-i")
    if params.get("outliers_check"):
        cargs.append("-oc")
    if params.get("slice_pattern") is not None:
        cargs.extend([
            "-sp",
            params.get("slice_pattern")
        ])
    if params.get("output_directory") is not None:
        cargs.extend([
            "-od",
            params.get("output_directory")
        ])
    return cargs


def v__rename_panga_outputs(
    params: VRenamePangaParameters,
    execution: Execution,
) -> VRenamePangaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VRenamePangaOutputs(
        root=execution.output_file("."),
        head_file=execution.output_file(params.get("output_directory") + "/" + params.get("output_root") + "_r#.HEAD") if (params.get("output_directory") is not None) else None,
        brik_file=execution.output_file(params.get("output_directory") + "/" + params.get("output_root") + "_r#.BRIK") if (params.get("output_directory") is not None) else None,
        log_file=execution.output_file(params.get("output_directory") + "/MAPLOG_Panga") if (params.get("output_directory") is not None) else None,
    )
    return ret


def v__rename_panga_execute(
    params: VRenamePangaParameters,
    execution: Execution,
) -> VRenamePangaOutputs:
    """
    Creates AFNI bricks from RealTime GE EPI series.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VRenamePangaOutputs`).
    """
    params = execution.params(params)
    cargs = v__rename_panga_cargs(params, execution)
    ret = v__rename_panga_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__rename_panga(
    dir_number: str,
    first_image_number: str,
    num_slices: float,
    num_reps: float,
    output_root: str,
    keep_prefix: bool = False,
    interactive: bool = False,
    outliers_check: bool = False,
    slice_pattern: str | None = None,
    output_directory: str | None = None,
    runner: Runner | None = None,
) -> VRenamePangaOutputs:
    """
    Creates AFNI bricks from RealTime GE EPI series.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dir_number: The directory number where the first image of the series is\
            stored.
        first_image_number: The number of the first image in the series.
        num_slices: The number of slices making up the imaged volume.
        num_reps: The number of samples in your time series.
        output_root: The prefix for the output brick.
        keep_prefix: Forces @RenamePanga to use the prefix you designate\
            without modification.
        interactive: Launches to3d in interactive mode. This allows you to\
            double check the automated settings.
        outliers_check: Performs outliers check and writes the outliers to a\
            .1D file placed in the output directory.
        slice_pattern: Sets the slice acquisition pattern. The default option\
            is alt+z.
        output_directory: Directory where the output (bricks and 1D files) will\
            be stored. The default directory is ./afni.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VRenamePangaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__RENAME_PANGA_METADATA)
    params = v__rename_panga_params(
        dir_number=dir_number,
        first_image_number=first_image_number,
        num_slices=num_slices,
        num_reps=num_reps,
        output_root=output_root,
        keep_prefix=keep_prefix,
        interactive=interactive,
        outliers_check=outliers_check,
        slice_pattern=slice_pattern,
        output_directory=output_directory,
    )
    return v__rename_panga_execute(params, execution)


__all__ = [
    "VRenamePangaOutputs",
    "VRenamePangaParameters",
    "V__RENAME_PANGA_METADATA",
    "v__rename_panga",
    "v__rename_panga_params",
]
